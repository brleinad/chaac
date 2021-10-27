import requests
from django.conf import settings


class OpenWeatherApi:

    BASE_URL = "api.openweathermap.org/data/2.5/"

    def get_weather_forecast(self, city, state, country, units):
        days = 5  # hardcoded for now
        endpoint = (
            f"{self.BASE_URL}forecast/daily?q={city},{state},{country}"
            f"&cnt={days}&units={units}&appid={settings.OPEN_WEATHER_KEY}"
        )
        response = requests.get(endpoint)
        print(f"OPEN WEATHER response: {response.text}")
        return response
