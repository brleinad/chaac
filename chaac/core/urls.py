from django.urls import path

from chaac.core.views import WeatherForecastView

urlpatterns = [path("", WeatherForecastView.as_view(), name="chaac")]
