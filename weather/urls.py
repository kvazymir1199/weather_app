from django.urls import path
from .views import MainView, WeatherForecastView

app_name = "weather"
urlpatterns = [
    path("", MainView.as_view(), name="index"),
    path("forecast/<str:city>", WeatherForecastView.as_view(), name="detail"),
]
