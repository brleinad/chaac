import requests
from django.conf import settings


class OpenWeatherMapApi:

    BASE_URL = "http://api.openweathermap.org"

    def get_weather_forecast(self, location, units="metric"):
        endpoint = (
            f"{self.BASE_URL}/data/2.5/onecall?lat={location.latitude}&lon={location.longitude}"
            f"&exclude=minutely,hourly"
            f"&units={units}&appid={settings.OPEN_WEATHER_MAP_KEY}"
        )
        response = requests.get(endpoint)
        # print(f"OPEN WEATHER response: {response.text}")
        return response

    def find_location(self, location_name):
        limit = 5  # hardcoded for now
        endpoint = (
            f"{self.BASE_URL}/geo/1.0/direct?q={location_name}&limit={limit}"
            f"&appid={settings.OPEN_WEATHER_MAP_KEY}"
        )
        response = requests.get(endpoint)
        print(f"OPEN WEATHER response: {response.text}")
        return response
