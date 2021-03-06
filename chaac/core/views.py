import datetime

from django.views.generic import CreateView, FormView

from chaac.core.forms import FindLocationForm
from chaac.core.models import Location, WeatherForecastPlan
from chaac.open_weather_map.api import OpenWeatherMapApi

open_weather_map_api = OpenWeatherMapApi()


class FindLocationView(FormView):
    template_name = "pages/app.html"
    form_class = FindLocationForm
    success_url = "/"

    def form_valid(self, form):
        location_name = form.cleaned_data["name"]
        response = open_weather_map_api.find_location(location_name)
        found_locations = response.json()
        self.request.session["found_locations"] = found_locations
        return super().form_valid(form)


class AddLocationView(CreateView):
    template_name = "pages/app.html"
    # form_class = AddLocationForm
    model = Location
    fields = ["name", "country_code", "plan", "longitude", "latitude"]
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        form_data = self.request.POST.copy()

        plan_id = self.request.session.get("plan_id", False)
        if not plan_id:
            plan = WeatherForecastPlan.objects.create()
            plan_id = str(plan.id)
            self.request.session["plan_id"] = plan_id
        form_data["plan"] = plan_id

        if self.request.method in ("POST", "PUT"):
            kwargs.update(
                {
                    "data": form_data,
                }
            )
        return kwargs


class WeatherForecastPlannerView(FormView):
    form_class = FindLocationForm
    template_name = "pages/app.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["found_locations"] = self.request.session.get("found_locations")
        self.request.session["found_locations"] = []  # reset for next search

        plan_id = self.request.session.get("plan_id")
        saved_locations = Location.objects.filter(plan_id=plan_id)

        locations = []
        for location in saved_locations:
            locations.append(
                {
                    "name": location.name,
                    "country": location.country_code,
                    "weather": self.get_weather_for_location(location),
                }
            )

        context["saved_locations"] = locations
        dates = []
        dates = [day.get("date") for day in locations[0].get("weather")]
        context["dates"] = dates

        print("locations: ", locations)

        return context

    def get_weather_for_location(self, location):
        response = open_weather_map_api.get_weather_forecast(location)
        forecasts = response.json().get("daily")

        day = 0
        weather = []
        for forecast in forecasts:
            weather.append(
                {
                    "date": datetime.datetime.fromtimestamp(forecast.get("dt")),
                    "day_temp": forecast.get("temp").get("day"),
                    "min_temp": forecast.get("temp").get("min"),
                    "max_temp": forecast.get("temp").get("max"),
                    "humidity": forecast.get("humidity"),
                    "conditions": forecast.get("weather")[0].get("description"),
                    "icon": forecast.get("weather")[0].get("icon"),
                }
            )
            day += 1
        return weather
