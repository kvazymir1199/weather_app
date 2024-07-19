from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class WeatherData(models.Model):
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    apparent_temperature = models.DecimalField(max_digits=10, decimal_places=2)
    precipitation = models.DecimalField(max_digits=10, decimal_places=2)
    is_day = models.BooleanField()
    wind_speed = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (f"temperature: {self.temperature}"
                f"humidity_2m: {self.humidity}"
                f"apparent_temperature: {self.apparent_temperature}"
                f"precipitationЖ {self.precipitation}"
                f"rain: {self.is_day}"
                f"wind_speed: {self.wind_speed}")
