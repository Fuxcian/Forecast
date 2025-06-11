# Parsing JSON from a weather API
import json
import ssl
from urllib.request import urlopen

def main():
    # Retrieve information from Muncie, IN
    location = "40.1934,-85.3864"
    url = f"https://api.weather.gov/points/{location}"
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    weatherData = json.loads(response.read())
    
    # Get the forecast URL from the properties object
    forecast_url = weatherData["properties"]["forecast"]

    # Fetch the 7-day 12-hour forecast
    forecast_response = urlopen(forecast_url, context=context)
    forecast_data = json.loads(forecast_response.read())

    # Loop through the periods and display required info
    periods = forecast_data["properties"]["periods"]
    for period in periods:
        print(f"Name: {period['name']}")
        print(f"Temperature: {period['temperature']} {period['temperatureUnit']}")
        print(f"Details: {period['detailedForecast']}\n")

main()