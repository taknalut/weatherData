import sys
import requests

def getWeatherForecast():
    #Handle a file open error
    try:
        location_data = open("location.txt", "r")
    except IOError:
        print("There was an error reading file")
        sys.exit()

    base_url = "https://api.weather.gov/points/"
    temperature = []

    for location in location_data:
        # extract latitude, longitude, and concate the url
        latitude = location.split(",")[0][:location.split(",")[0].index("°")].strip()
        longitude = location.split(",")[1][:location.split(",")[1].index("°")].strip()
        if len(latitude) == 7 and len(latitude) == 7:
            url = base_url + latitude + ",-" + longitude
        
        # call weather.gov API
        response = requests.get(url)
        if response.status_code == 200:
            raw_data = response.json()

        # extract the forecast url and make a call to the forecast endpoint
        forecast_url = raw_data['properties']['forecast']
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
        
        # extract the temperature for the "Wednesday Night"
        periods = forecast_data['properties']['periods']
        for obj in periods:
            if obj['name'] == 'Wednesday Night':
                temperature.append(obj['temperature'])
    
    output = ", ".join(str(temp) for temp in temperature)
    print(output)


getWeatherForecast()