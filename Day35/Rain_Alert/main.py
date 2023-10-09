import requests

parameters = {
    "lat": 52.229675,
    "lon": 21.012230,
    "exclude": "current,minutely,daily,alerts",
    "appid": "",
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")






