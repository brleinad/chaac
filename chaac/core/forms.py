from django import forms

from chaac.core.models import Location
from chaac.open_weather_map.api import OpenWeatherMapApi

open_weather_map_api = OpenWeatherMapApi()


class FindLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name"]

    def save(self, commit=True):
        # super().save()
        pass  # Don't save the model


class AddLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "country_code", "plan"]
