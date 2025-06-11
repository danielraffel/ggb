import os
import requests
from datetime import datetime, timedelta
from pytz import timezone, utc
from astral.sun import sun
from astral import LocationInfo
import sys

# Inputs
repo = os.getenv("GITHUB_REPO")  # e.g. "danielraffel/ggb"
file_path = os.getenv("IMAGE_PATH", "ggb.screenshot.png")
branch = os.getenv("BRANCH", "main")
token = os.getenv("GITHUB_TOKEN")

latitude = float(os.getenv("LATITUDE", "37.8199"))
longitude = float(os.getenv("LONGITUDE", "-122.4783"))
tz = os.getenv("TIMEZONE", "America/Los_Angeles")

# GitHub API URL
headers = {"Authorization": f"Bearer {token}"}
url = f"https://api.github.com/repos/{repo}/commits?path={file_path}&sha={branch}&per_page=1"

res = requests.get(url, headers=headers)
if res.status_code != 200:
    print(f"::error::GitHub API error: {res.status_code}")
    sys.exit(1)

data = res.json()
if not data:
    print("::error::No commits found for file.")
    sys.exit(1)

commit_time_str = data[0]["commit"]["committer"]["date"]  # UTC time
last_modified = datetime.strptime(commit_time_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc)

# Local time
local_tz = timezone(tz)
now_local = datetime.now(local_tz)
now_utc = now_local.astimezone(utc)

# Sun times
city = LocationInfo(latitude=latitude, longitude=longitude)
sun_times = sun(city.observer, date=now_local.date(), tzinfo=local_tz)
sunrise_utc = sun_times["sunrise"].astimezone(utc)
civil_twilight_utc = sun_times["dusk"].astimezone(utc)

# Logic
stale = now_utc - last_modified > timedelta(minutes=30)
in_window = sunrise_utc <= now_utc <= civil_twilight_utc

print(f"::notice::Last updated: {last_modified}")
print(f"::notice::Now: {now_utc}")
print(f"::notice::Stale: {stale}, In window: {in_window}")

if stale and in_window:
    print("::set-output name=stale::true")
    sys.exit(0)
else:
    print("::set-output name=stale::false")
    sys.exit(0)
