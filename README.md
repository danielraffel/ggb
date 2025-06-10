**TL;DR:** Visit [danielraffel.github.io/ggb](https://danielraffel.github.io/ggb) to check today’s weather conditions for crossing the Golden Gate Bridge.

# Best Times to Cross the Golden Gate Bridge Today, Based on Weather Conditions

I frequently ride across the Golden Gate Bridge and wanted an easy way to check current and future weather conditions so I could dress appropriately. This site provides real-time weather updates along with a customizable forecast for both crossings. It’s ideal for cyclists, runners, and walkers who want to plan their trip based on accurate weather data.

## How to View It

Visit [danielraffel.github.io/ggb](https://danielraffel.github.io/ggb) to view the live stream, check current weather conditions, and access a future weather forecast. The site displays key information such as temperature, wind speed, rain probability, and sunset time. It also suggests the best two times for your crossings today, helping you choose the optimal windows for your trip.

If you typically start from the same location, you can set time offsets to match your usual travel times. These settings are saved in your browser’s local storage, so the site automatically adjusts the forecast for both your outbound and return crossings without requiring any input each time you visit.

## Key Features

* **Real-Time Weather Conditions**: Current temperature, wind speed, rain probability, and sunset time, updated every 10 minutes.
* **Future Weather Forecast**: By default, the forecast is set for 2 hours ahead, but you can adjust the time to match your ride. The site suggests the best two crossing windows based on today’s forecast.
* **Time Offsets**: Set custom time offsets for both outbound and return trips. These offsets are saved in local storage and automatically applied on your next visit.
* **Screenshot from Live Web Cam**: A screenshot from the Golden Gate Bridge webcam is captured every 5 minutes, documenting its visual condition. Screenshots are updated only between sunrise and civil twilight PST (eg after the sun has set \~6 degrees below the horizon); at night, from civil twilight to sunrise, updates are paused.
* **Sunset Time**: Automatically shows today’s sunset time, helping you plan for daylight hours.

## How It Was Built

* **HTML5**: Provides the structure for the page.
* **[Tailwind CSS](https://tailwindcss.com)**: Ensures a responsive and mobile-friendly design.
* **[Axios](https://axios-http.com/docs/intro)**: Used to fetch real-time weather data from the [Open-Meteo API](https://open-meteo.com/en/docs).
* **JavaScript**: Dynamically updates weather conditions every 10 minutes without needing a page refresh.
* **Local Storage**: Saves your time offset settings so they are applied automatically during future visits.
* **N8N Workflow**: Runs a cron that uses browserless and Playwright to clip the GGB webcam page and upload the screenshot to this repo every 5 minutes between 5am and 8pm PST.

## Screenshot from Live Web Cam

A screenshot from the Golden Gate Bridge webcam is captured every 5 minutes, documenting its visual condition.

* **Timing**: Screenshots are only generated between **sunrise** and **[civil sunset](https://en.wikipedia.org/wiki/Twilight#Civil_twilight)** (when the sun is \~6° below the horizon).
* **Nighttime Pause**: From **civil sunset to sunrise**, screenshot generation is paused to avoid capturing dark, low-visibility images.
* **Failsafe Detection**: If a screenshot is accidentally captured with a white UI bar or is fully black, a validator automatically detects the issue and triggers a retry via a secure n8n webhook.
* **Regular Cadence**: Unless an issue is detected, screenshots are consistently captured and committed to the repo every **5 minutes** during daylight hours.

## Screenshot Quality Validator (via GitHub Actions)

To ensure screenshot quality and avoid uploading bad or unusable webcam images (e.g., black frames or white UI bars), this repo includes a GitHub Action that runs on every `ggb.screenshot.png` update. Here’s how it works:

* A Python script (`detect_screenshot.py`) is triggered when the screenshot is updated.
* The script analyzes the image for:

  * **Top white bars**
  * **Bottom white bars**
  * **Completely black images**
* If any of these conditions are detected, the script triggers a **secure webhook** to a production [n8n](https://n8n.io) instance, which re-runs the screenshot job automatically.

## Secrets and Webhook Security

Since this repository is public, sensitive details like authentication secrets are **not hardcoded** in the script or action. Instead:

* A secret token is stored securely in GitHub under **Settings → Secrets and variables → Actions** (e.g., `GGB_WEBHOOK_SECRET`).
* The webhook URL is protected using a custom `x-ggb-auth` header that the Python script includes with every POST.
* The n8n workflow is configured to **validate this secret** before executing any job logic.
* This prevents abuse by ensuring only trusted automation (i.e., from this GitHub Action) can trigger workflows.

## Additional Features

* **Crossing Time Adjustment**: You can enter times for both crossings. The site will display weather forecasts for both your outbound and return trips, factoring in the time it takes to reach the bridge.
* **Suggested Crossing Times**: The site provides the best two times to cross the bridge today, based on the forecasted conditions.
* **Night Mode**: The site automatically switches to a dark theme between 8 PM and 6 AM for better visibility in low-light conditions.

## FYI:

Weather is only displayed for the current day, from 12:00 AM to 11:59 PM.

## Final Notes

I developed two slightly different versions of the site:

* **[The Best Time for Athletes to Cross the Golden Gate Bridge Today](https://danielraffel.github.io/ggb)** is designed for cyclists and runners who want to:

  * View a real-time image of the bridge
  * Check the weather conditions for their crossings
  * Access a daily forecast
  * Get recommendations for the best times to cross

* **[Golden Gate Bridge Weather Forecast for Cyclists and Runners](https://danielraffel.github.io/ggb/crossingforecast.html)** is designed for cyclists and runners who know when they are cycling and just want to:

  * View a real-time image of the bridge
  * Check the expected weather for their planned crossings
