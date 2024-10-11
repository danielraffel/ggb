# Golden Gate Bridge Live Weather Viewer

I frequently ride across the Golden Gate Bridge and wanted an easy way to check the current and future conditions so that I can dress appropriately. This page offers a live view of the Golden Gate Bridge along with real-time weather updates and a default two-hour forecast. You can check the current temperature, wind speed, and chance of rain, and if you’re planning to ride back across, you can adjust the forecast time for future weather predictions.

## How to View It

Simply visit [danielraffel.github.io/ggb](https://danielraffel.github.io/ggb) in your browser to view the live stream, current weather conditions, and a future weather forecast 2 hours from now (which you can adjust).

## How It Was Built

- **HTML5** for structuring the page.
- **[Tailwind CSS](https://tailwindcss.com)** for responsive design.
- **[Axios](https://axios-http.com/docs/intro)** allows real-time weather data fetching from the [Open-Meteo API](https://open-meteo.com/en/docs).
- **JavaScript** updates the weather widgets every 10 minutes, keeping the data fresh without needing a page refresh. It also generates a default weather forecast for 2 hours into the future, which users can modify.

## What It Does

The page displays:

- **Live Stream**: A [live video feed of the Golden Gate Bridge](https://www.iplivecams.com/live-cams/golden-gate-bridge-san-francisco-california-united-states/).
- **Real-Time Weather Updates**: 
  - Current temperature (in Fahrenheit)
  - Wind speed (in mph)
  - Probability of rain based on real-time data from the Open-Meteo API
- **Future Weather Forecast**: 
  - By default, a 2-hour future forecast is displayed, showing the temperature, wind speed, and likelihood of rain. Users can adjust the time to see weather conditions at different hours.

The weather information is fetched for the Golden Gate Bridge area (latitude: 37.8199, longitude: -122.4783), and is updated every 10 minutes. The future forecast is automatically set for 2 hours into the future but can be adjusted using the input field.

## Example Output

```html
<p>Temperature: 65°F</p>
<p>Wind Speed: 10 mph</p>
<p>Likely to Rain: No (15% chance)</p>

<p>Future Weather (in 2 hours):</p>
<p>Temperature: 60°F</p>
<p>Wind Speed: 8 mph</p>
<p>Likely to Rain: Yes (40% chance)</p>
```
