import uuid

from django.db import models


class WeatherForecastPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Location(models.Model):
    name = models.CharField(max_length=128)
    country_code = models.CharField(max_length=2)
    plan = models.ForeignKey(WeatherForecastPlan, on_delete=models.CASCADE)
