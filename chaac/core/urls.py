from django.urls import path

from chaac.core.views import FindLocationView, WeatherForecastPlannerView

urlpatterns = [
    path("find/", FindLocationView.as_view(), name="find"),
    path("", WeatherForecastPlannerView.as_view(), name="chaac"),
]
