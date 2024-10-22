**TL;DR:** Visit [danielraffel.github.io/ggb](https://danielraffel.github.io/ggb) to check today’s weather conditions for crossing the Golden Gate Bridge.

# Best Times to Cross the Golden Gate Bridge Today, Based on Weather Conditions
I frequently ride across the Golden Gate Bridge and wanted an easy way to check current and future weather conditions so I could dress appropriately. This site provides real-time weather updates along with a customizable forecast for both crossings. It’s ideal for cyclists, runners, and walkers who want to plan their trip based on accurate weather data.

## How to View It
Visit [danielraffel.github.io/ggb](https://danielraffel.github.io/ggb) to view the live stream, check current weather conditions, and access a future weather forecast. The site displays key information such as temperature, wind speed, rain probability, and sunset time. It also suggests the best two times for your crossings today, helping you choose the optimal windows for your trip.

If you typically start from the same location, you can set time offsets to match your usual travel times. These settings are saved in your browser’s local storage, so the site automatically adjusts the forecast for both your outbound and return crossings without requiring any input each time you visit.

## Key Features
- **Real-Time Weather Conditions**: Current temperature, wind speed, rain probability, and sunset time, updated every 10 minutes.
- **Future Weather Forecast**: By default, the forecast is set for 2 hours ahead, but you can adjust the time to match your ride. The site suggests the best two crossing windows based on today’s forecast.
- **Time Offsets**: Set custom time offsets for both outbound and return trips. These offsets are saved in local storage and automatically applied on your next visit.
- **Live Stream**: A live video feed of the Golden Gate Bridge to help you assess conditions visually.
- **Sunset Time**: Automatically shows today’s sunset time, helping you plan for daylight hours.

## How It Was Built
- **HTML5**: Provides the structure for the page.
- **[Tailwind CSS](https://tailwindcss.com)**: Ensures a responsive and mobile-friendly design.
- **[Axios](https://axios-http.com/docs/intro)**: Used to fetch real-time weather data from the [Open-Meteo API](https://open-meteo.com/en/docs).
- **JavaScript**: Dynamically updates weather conditions every 10 minutes without needing a page refresh.
- **Local Storage**: Saves your time offset settings so they are applied automatically during future visits.

## Additional Features
- **Crossing Time Adjustment**: You can enter times for both crossings. The site will display weather forecasts for both your outbound and return trips, factoring in the time it takes to reach the bridge.
- **Suggested Crossing Times**: The site provides the best two times to cross the bridge today, based on the forecasted conditions.
- **Night Mode**: The site automatically switches to a dark theme between 8 PM and 6 AM for better visibility in low-light conditions.

## Final Notes
In addition to the [main site](https://danielraffel.github.io/ggb), I’ve created a couple of other versions to suit different audiences:
- **[The Golden Gate Bridge Weather Forecast for Cyclists and Runners](https://danielraffel.github.io/ggb/crossingforecast.html)** is designed for athletes who know how long it takes to reach the bridge and just want a forecast for their planned crossing times.
- **[The Best Time for Visitors to SF to Plan to Cross the Golden Gate Bridge Today](https://danielraffel.github.io/ggb/planvisit.html)** is ideal for tourists who want to quickly find the best time to cross the bridge based on forecasted weather conditions.
