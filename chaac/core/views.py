# from django.urls import reverse
from django.views.generic import FormView

from chaac.core.forms import WeatherForecastForm


class WeatherForecastView(FormView):
    form_class = WeatherForecastForm
    template_name = "pages/app.html"
    success_url = "/"  # reverse('chaac')
