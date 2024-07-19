import time
import requests
import openmeteo_requests
import requests_cache
from dataclasses import dataclass
from functools import wraps
from django.http import HttpResponseNotFound, Http404
from rest_framework.exceptions import NotFound
from .serializers import CitySerializer
from .models import WeatherData
from retry_requests import retry

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
    res = get_city_list(name)
    print(res)
    return res


def get_cities_by_name(name):
    return get_city_list(name, many=True)


def get_city_list(name, many=False):
    url = 'https://geocoding-api.open-meteo.com/v1/search'
    response = requests.get(url, params=CityRequest(name=name).__dict__).json()
    result = response.get("results")
    if not result:
        raise NotFound("City not founded")

    serializer = CitySerializer(data=result if many else result[0], many=many)

    if serializer.is_valid():
        return serializer.data
    raise Http404


def get_weather_forecast(city) -> WeatherData | None:
    try:
        data = get_city_by_name(city)
        url = "https://api.open-meteo.com/v1/forecast"
        if not data:
            return None
        params = ForecastRequest(**data)
        response = openmeteo.weather_api(url, params=params.__dict__)[0]
        current = response.Current()
        return WeatherData(
            temperature=current.Variables(0).Value(),
            humidity=current.Variables(1).Value(),
            apparent_temperature=current.Variables(2).Value(),
            precipitation=current.Variables(3).Value(),
            is_day=current.Variables(4).Value(),
            wind_speed=current.Variables(5).Value()
        )
    except NotFound:
        HttpResponseNotFound("hello")


def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Начало времени
        result = func(*args, **kwargs)  # Выполнение функции
        end_time = time.time()  # Конец времени
        elapsed_time = end_time - start_time  # Расчет времени выполнения
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds")
        return result

    return wrapper

#
