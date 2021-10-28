from django import forms

from chaac.core.models import Location
from chaac.open_weather_map.api import OpenWeatherMapApi

open_weather_map_api = OpenWeatherMapApi()


class FindLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name"]

    # def clean(self):
    #     location_name = self.cleaned_data['name']
    #     response = open_weather_map_api.find_location(location_name)
    #     found_locations = response.json()
    #     print(found_locations)

    def save(self, commit=True):
        # super().save()
        pass  # Don't save the model
