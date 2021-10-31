from django.contrib import admin

from chaac.core.models import Location, WeatherForecastPlan

admin.site.register(WeatherForecastPlan)
admin.site.register(Location)
