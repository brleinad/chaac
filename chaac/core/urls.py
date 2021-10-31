from django.urls import path

from chaac.core.views import (
    AddLocationView,
    FindLocationView,
    WeatherForecastPlannerView,
)

urlpatterns = [
    path("find/", FindLocationView.as_view(), name="find"),
    path("add/", AddLocationView.as_view(), name="add"),
    path("", WeatherForecastPlannerView.as_view(), name="chaac"),
]
