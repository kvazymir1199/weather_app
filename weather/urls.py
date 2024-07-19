import regex as re
from django.urls import path,re_path
from .views import MainView, WeatherForecastView

app_name = "weather"
urlpatterns = [
    path("", MainView.as_view(), name="index"),
    path("forecast/<str:city>", WeatherForecastView.as_view(), name="detail"),
]
