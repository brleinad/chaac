from django.views.generic import FormView, TemplateView

from chaac.core.forms import FindLocationForm
from chaac.open_weather_map.api import OpenWeatherMapApi

open_weather_map_api = OpenWeatherMapApi()


class FindLocationView(FormView):
    template_name = "app/find_location.html"
    form_class = FindLocationForm
    success_url = "/find/"
    found_locations = []

    def form_valid(self, form):
        location_name = form.cleaned_data["name"]
        response = open_weather_map_api.find_location(location_name)
        found_locations = response.json()
        print(found_locations)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[found_locations] =
        return context


class WeatherForecastPlannerView(TemplateView):
    # form_class = WeatherForecastForm
    template_name = "pages/app.html"
    success_url = "/"  # reverse('chaac')
