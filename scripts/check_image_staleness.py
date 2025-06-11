import os
import requests
from datetime import datetime, timedelta
from pytz import timezone, utc
from astral.sun import sun
from astral import LocationInfo
import sys

# Config
image_url = os.getenv("IMAGE_URL")
latitude = float(os.getenv("LATITUDE", "37.8199"))
longitude = float(os.getenv("LONGITUDE", "-122.4783"))
tz = os.getenv("TIMEZONE", "America/Los_Angeles")

# Get current local time
local_tz = timezone(tz)
now_local = datetime.now(local_tz)
now_utc = now_local.astimezone(utc)

# Get sunrise and civil twilight in UTC
city = LocationInfo(latitude=latitude, longitude=longitude)
sun_times = sun(city.observer, date=now_local.date(), tzinfo=local_tz)
sunrise_utc = sun_times["sunrise"].astimezone(utc)
civil_twilight_utc = sun_times["dusk"].astimezone(utc)

# Get image last modified time
res = requests.head(image_url)
last_modified_str = res.headers.get("Last-Modified")

if not last_modified_str:
    print("::error::Missing Last-Modified header in image.")
    sys.exit(1)

last_modified = datetime.strptime(last_modified_str, '%a, %d %b %Y %H:%M:%S %Z').replace(tzinfo=utc)

# Logic: stale if older than 30 min and within sunrise-civil twilight
stale = now_utc - last_modified > timedelta(minutes=30)
in_time_window = sunrise_utc <= now_utc <= civil_twilight_utc

if stale and in_time_window:
    print("::notice::Image is stale and in time window. Triggering restart.")
    print("::set-output name=stale::true")
    sys.exit(0)
else:
    print("::notice::Image is fresh or outside time window.")
    print("::set-output name=stale::false")
    sys.exit(0)
