import requests
import openmeteo_requests
import requests_cache
from dataclasses import dataclass
from django.http import Http404
from .serializers import CitySerializer
from .models import WeatherData, CityData
from retry_requests import retry
from django.core.exceptions import ObjectDoesNotExist

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)


@dataclass
class CityRequest:
    name: str
    language: str = "ru"
    count: int = 1
    format: str = "json"


@dataclass
class ForecastRequest:
    latitude: str
    longitude: str
    timezone: str
    current: list[str] = None

    def __post_init__(self):
        if self.current is None:
            self.current = [
                "temperature_2m",
                "relative_humidity_2m",
                "apparent_temperature",
                "precipitation",
                "is_day",
                "wind_speed_10m"
            ]


def get_city_by_name(name):
    try:
        city = CityData.objects.get(slug=name.lower())
        return city
    except CityData.DoesNotExist:
        url = 'https://geocoding-api.open-meteo.com/v1/search'
        response = requests.get(url, params={'name': name}).json()
        result = response.get("results")
        if not result:
            raise ObjectDoesNotExist

        result[0]["slug"] = name.lower()
        serializer = CitySerializer(data=result[0])

        if serializer.is_valid():
            serializer.save()
            return CityData.objects.get(slug=name.lower())
        else:
            print("Serializer not valid", serializer.errors)
            raise Http404


def get_weather_forecast(city) -> WeatherData | None:
    try:
        data = get_city_by_name(city)
        url = "https://api.open-meteo.com/v1/forecast"
        if not data:
            raise ObjectDoesNotExist
        params = ForecastRequest(latitude=data.latitude,
                                 longitude=data.longitude,
                                 timezone=data.timezone)
        response = openmeteo.weather_api(url, params=params.__dict__)[0]
        current = response.Current()
        weather_data = WeatherData(
            temperature=current.Variables(0).Value(),
            humidity=current.Variables(1).Value(),
            apparent_temperature=current.Variables(2).Value(),
            precipitation=current.Variables(3).Value(),
            is_day=current.Variables(4).Value(),
            wind_speed=current.Variables(5).Value(),
            city=data
        )
        weather_data.save()
        return weather_data
    except ObjectDoesNotExist:
        return None
