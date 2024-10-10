# Golden Gate Bridge Live Weather Viewer

I frequently ride across the bridge and wanted an easy way to check the current conditions. This page provides a live view of the Golden Gate Bridge along with real-time weather updates. You can view the current temperature, wind speed, and likelihood of rain directly from your web browser.

## How to View It

Simply visit [danielraffel.github.io/ggb](https://danielraffel.github.io/ggb) in your browser to view the live stream and current weather conditions.

## How It Was Built

- **HTML5** was used for structuring the page.
- **Tailwind CSS** powers the responsive and modern design.
- **Axios** allows real-time weather data fetching from the Open-Meteo API.
- **JavaScript** updates the weather widget every 10 minutes, keeping the data fresh without needing a page refresh.

## What It Does

The page displays:

- **Live Stream**: A live video feed of the Golden Gate Bridge.
- **Real-Time Weather Updates**: 
  - Current temperature (in Fahrenheit)
  - Wind speed (in mph)
  - Probability of rain based on real-time data from the Open-Meteo API

The weather information is fetched for the Golden Gate Bridge area (latitude: 37.8199, longitude: -122.4783), and is updated every 10 minutes.

## Example Output

```html
<p>Temperature: 65°F</p>
<p>Wind Speed: 10 mph</p>
<p>Likely to Rain: No (15% chance)</p>
```
