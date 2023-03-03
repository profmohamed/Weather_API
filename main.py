import requests
import json

# api-endpoint put your link here
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

# put your api key here

api_key = "####################"
weather_params = {
    "lat": 30.044420,
    "lon": 31.235712,
    "appid": api_key,

}

response = requests.get(OWN_ENDPOINT, params=weather_params)
print(response.status_code)
print(response.json())
