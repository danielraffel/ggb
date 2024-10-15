# Golden Gate Bridge Live Weather Viewer

I frequently ride across the Golden Gate Bridge and wanted an easy way to check the current and future conditions so that I can dress appropriately. This page offers a live view of the Golden Gate Bridge along with real-time weather updates and a customizable future weather forecast. You can check the current temperature, wind speed, and chance of rain, and if you’re planning to ride back across, you can adjust the forecast time based on when you think you'll be riding back across.

## How to View It

Simply visit [danielraffel.github.io/ggb](https://danielraffel.github.io/ggb) in your browser to view the live stream, current weather conditions, and a future weather forecast, which can be adjusted to match your ride. The default forecast time is 2 hours ahead, but you can easily change it to see weather conditions at any time during your ride. If you frequently start from the same location, the site will remember the last time difference you set and automatically apply it to the future forecast, overriding the 2-hour default. This makes it convenient to use as a starting page before your ride, without needing to adjust it every time.

## How It Was Built

- **HTML5** for structuring the page.
- **[Tailwind CSS](https://tailwindcss.com)** for responsive design.
- **[Axios](https://axios-http.com/docs/intro)** for real-time weather data fetching from the [Open-Meteo API](https://open-meteo.com/en/docs).
- **JavaScript** to update the weather widgets dynamically every 10 minutes, keeping the data fresh without requiring a page refresh.
- **Local Storage** is used to save your time difference setting, enabling the weather forecast to display based on your customized time preference.

## What It Does

The page displays:

- **Live Stream**: A live video feed of the Golden Gate Bridge.
- **Real-Time Weather Updates**: 
  - Current temperature (in Fahrenheit)
  - Wind speed (in mph)
  - Probability of rain based on real-time data from the Open-Meteo API
- **Future Weather Forecast**: 
  - By default, a 2-hour future forecast is displayed, showing the temperature, wind speed, and likelihood of rain. Users can adjust the time input field to see weather conditions at different times.
  - A time difference display shows how far in the future the selected weather forecast is (e.g., "in 2h").

## Additional Features

- **Crossing Time Adjustment**: 
  - Users can enter a time for their first crossing and the app will automatically calculate and display weather conditions for the second crossing. The interface allows for precise control using either text input or dropdowns for hours and minutes.
  
- **Sunset Information**: 
  - Displays the time of sunset for the current or next day based on real-time data from Open-Meteo.

- **Mobile and Desktop Support**: 
  - The page adapts to mobile and desktop displays, allowing users to either enter or select times using dropdowns on mobile or type directly on desktop.
  
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

This app provides riders with all the information needed to plan their crossing safely, based on up-to-the-minute weather data.
