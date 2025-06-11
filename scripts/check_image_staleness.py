import os
import requests
from datetime import datetime, timedelta
from pytz import timezone, utc
from astral.sun import sun
from astral import LocationInfo
import sys

# Environment variables
repo = os.getenv("GITHUB_REPO")            # e.g. "danielraffel/ggb"
file_path = os.getenv("IMAGE_PATH")        # e.g. "ggb.screenshot.png"
branch = os.getenv("BRANCH", "main")       # e.g. "main"
token = os.getenv("GITHUB_TOKEN")
latitude = float(os.getenv("LATITUDE", "37.8199"))
longitude = float(os.getenv("LONGITUDE", "-122.4783"))
tz = os.getenv("TIMEZONE", "America/Los_Angeles")

# GitHub API request to get last commit for the file
headers = {"Authorization": f"Bearer {token}"}
api_url = f"https://api.github.com/repos/{repo}/commits?path={file_path}&sha={branch}&per_page=1"
response = requests.get(api_url, headers=headers)

if response.status_code != 200:
    print(f"::error::GitHub API error: {response.status_code}")
    sys.exit(1)

data = response.json()
if not data:
    print("::error::No commits found for file.")
    sys.exit(1)

commit_time_utc = datetime.strptime(data[0]["commit"]["committer"]["date"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=utc)

# Get current time in UTC
local_tz = timezone(tz)
now_local = datetime.now(local_tz)
now_utc = now_local.astimezone(utc)

# Calculate sunrise and civil twilight (dusk) for today in UTC
city = LocationInfo(latitude=latitude, longitude=longitude)
sun_times = sun(city.observer, date=now_local.date(), tzinfo=local_tz)
sunrise_utc = sun_times["sunrise"].astimezone(utc)
civil_twilight_utc = sun_times["dusk"].astimezone(utc)

# Decision logic
is_stale = now_utc - commit_time_utc > timedelta(minutes=30)
in_daylight = sunrise_utc <= now_utc <= civil_twilight_utc

# Output for logging
print(f"::notice::File last updated: {commit_time_utc}")
print(f"::notice::Current time: {now_utc}")
print(f"::notice::Sunrise: {sunrise_utc}, Civil Twilight: {civil_twilight_utc}")
print(f"::notice::Is stale? {is_stale}, In daylight window? {in_daylight}")

# Write result to GITHUB_OUTPUT
with open(os.environ["GITHUB_OUTPUT"], "a") as output:
    output.write(f"stale={'true' if is_stale and in_daylight else 'false'}\n")
