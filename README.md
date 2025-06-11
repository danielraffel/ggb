**TL;DR:** Visit [danielraffel.github.io/ggb](https://danielraffel.github.io/ggb) to check today's weather conditions for crossing the Golden Gate Bridge.

# Best Times to Cross the Golden Gate Bridge Today, Based on Weather Conditions

I frequently ride across the Golden Gate Bridge and wanted an easy way to check current and future weather conditions so I could dress appropriately. This site provides real-time weather updates along with a customizable forecast for both crossings. It's ideal for cyclists, runners, and walkers who want to plan their trip based on accurate weather data.

## How to View It

Visit [danielraffel.github.io/ggb](https://danielraffel.github.io/ggb) to view the live stream, check current weather conditions, and access a future weather forecast. The site displays key information such as temperature, wind speed, rain probability, and sunset time. It also suggests the best two times for your crossings today, helping you choose the optimal windows for your trip.

If you typically start from the same location, you can set time offsets to match your usual travel times. These settings are saved in your browser's local storage, so the site automatically adjusts the forecast for both your outbound and return crossings without requiring any input each time you visit.

## Key Features

* **Real-Time Weather Conditions**: Current temperature, wind speed, rain probability, and sunset time, updated every 10 minutes.
* **Future Weather Forecast**: By default, the forecast is set for 2 hours ahead, but you can adjust the time to match your ride. The site suggests the best two crossing windows based on today's forecast.
* **Time Offsets**: Set custom time offsets for both outbound and return trips. These offsets are saved in local storage and automatically applied on your next visit.
* **Screenshot from Live Web Cam**: A screenshot from the Golden Gate Bridge webcam is captured every 5 minutes, documenting its visual condition. Screenshots are updated only between sunrise and civil twilight end PST; at night, from civil twilight to sunrise, updates are paused.
* **Sunset Time**: Automatically shows today's sunset time, helping you plan for daylight hours.

## How It Was Built

* **HTML5**: Provides the structure for the page.
* **[Tailwind CSS](https://tailwindcss.com)**: Ensures a responsive and mobile-friendly design.
* **[Axios](https://axios-http.com/docs/intro)**: Used to fetch real-time weather data from the [Open-Meteo API](https://open-meteo.com/en/docs).
* **JavaScript**: Dynamically updates weather conditions every 10 minutes without needing a page refresh.
* **Local Storage**: Saves your time offset settings so they are applied automatically during future visits.
* **N8N Workflow**: Runs a scheduled automation using browserless and Playwright to capture the GGB webcam page and upload screenshots to this repo every 5 minutes during daylight hours.
* **Python Script**: Validates screenshot quality using image analysis with PIL and NumPy libraries.
* **GitHub Actions**: Automatically triggers validation workflow when new screenshots are uploaded.

## Screenshot from Live Web Cam

A screenshot from the Golden Gate Bridge webcam is captured every 5 minutes, documenting its visual condition.

* **Timing**: Screenshots are only generated between **sunrise** and **civil twilight end** (when the sun is approximately 6° below the horizon, as defined by the [sunrise-sunset.org API](https://sunrise-sunset.org/api)).
* **Coordinates**: Uses Golden Gate Bridge coordinates (37.8199°N, 122.4783°W) for precise sunrise/civil twilight calculations.
* **Fallback Logic**: If the API is unavailable, the system uses mathematical calculations with a 30-minute buffer after sunset for civil twilight approximation.
* **Nighttime Pause**: From **civil twilight end to sunrise**, screenshot generation is paused to avoid capturing dark, low-visibility images that offer little value.
* **Staging Process**: Screenshots are first uploaded to `staging.ggb.screenshot.png` for validation before being promoted to the final `ggb.screenshot.png` file.
* **Failsafe Detection**: If a screenshot is accidentally captured with a white UI bar or is fully black, a validator automatically detects the issue and triggers a retry via a secure n8n webhook.
* **Regular Cadence**: Unless an issue is detected, screenshots are consistently captured and committed to the repo every **5 minutes** during daylight hours.

## Screenshot Quality Validator with Staging Workflow (via GitHub Actions)

To ensure screenshot quality and avoid displaying bad or unusable webcam images (e.g., black frames or white UI bars), this repo includes a staging and validation workflow:

### Staging Process

1. **Initial Upload**: The n8n workflow uploads new screenshots to `staging.ggb.screenshot.png`
2. **Automatic Validation**: A GitHub Action is triggered when the staging file is updated
3. **Quality Check**: A Python script (`detect_screenshot.py`) analyzes the staging image for:
   * **Top white bars** (>95% white pixels in top 100 pixels)
   * **Bottom white bars** (>95% white pixels in bottom 100 pixels)
   * **Completely black images** (>95% black pixels overall)
4. **Promotion or Retry**: 
   * If the image passes validation, it's automatically copied to `ggb.screenshot.png` (the live file) using the GitHub API
   * If validation fails, a **secure webhook** triggers the n8n workflow to capture a new image
   * The staging file remains for the next upload, ensuring no broken workflow states

### Benefits of Staging Workflow

* **No Bad Images**: Users never see invalid screenshots since only validated images are promoted to the live file
* **Automatic Recovery**: Failed validations automatically trigger retries without manual intervention
* **Persistent Staging**: The staging file persists between uploads, preventing workflow conflicts
* **Clean Separation**: Clear distinction between incoming (staging) and live (final) screenshot files
* **GitHub API Integration**: Uses GitHub's REST API for secure file operations with proper authentication

### Security Implementation

Since this repository is public, sensitive details like authentication secrets are **not hardcoded** in the script or action. Instead:

* Secret tokens are stored securely in GitHub under **Settings → Secrets and variables → Actions** (e.g., `GGB_WEBHOOK_SECRET`, `GGB_WEBHOOK_URL`)
* The webhook URL is protected using a custom `x-ggb-auth` header that the Python script includes with every POST
* The n8n workflow is configured to **validate this secret** before executing any job logic
* GitHub API operations use the built-in `GITHUB_TOKEN` with appropriate `contents: write` permissions
* This prevents abuse by ensuring only trusted automation (i.e., from this GitHub Action) can trigger workflows

## Additional Features

* **Crossing Time Adjustment**: You can enter times for both crossings. The site will display weather forecasts for both your outbound and return trips, factoring in the time it takes to reach the bridge.
* **Suggested Crossing Times**: The site provides the best two times to cross the bridge today, based on the forecasted conditions.
* **Night Mode**: The site automatically switches to a dark theme between 8 PM and 6 AM (20:00-06:00) for better visibility in low-light conditions.

## FYI:

Weather is only displayed for the current day, from 12:00 AM to 11:59 PM.

## Coming Soon

An **iOS app** is currently in development, featuring:
* Live monitoring widget for quick weather checks
* Commuter widget with daily ride info 

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
