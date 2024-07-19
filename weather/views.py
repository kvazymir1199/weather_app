from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from .forms import SearchForm
from .utils import get_weather_forecast
import urllib.parse


class MainView(FormMixin, TemplateView):
    template_name = "weather/index.html"
    form_class = SearchForm

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        last_visited_pages = request.session.get('last_visited_pages', [])
        if last_visited_pages:
            last_viewed = last_visited_pages[0].get("path")
            if request.path != last_viewed:
                return redirect(last_viewed)
        return TemplateResponse(request,
                                "weather/index.html",
                                context={"form": form})

    def post(self, request, *args, **kwargs):
        return send_search_request(self, request, *args, **kwargs)


class WeatherForecastView(TemplateView, FormMixin):
    template_name = "weather/forecast.html"
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        query = urllib.parse.unquote(kwargs.get("city", ''))
        context = super().get_context_data(**kwargs)
        context['title'] = query
        return context

    def get(self, request, *args, **kwargs):
        query = urllib.parse.unquote(kwargs.get("city", ''))

        forecast = get_weather_forecast(query)

        context = {
            "forecast": forecast,
            "form": self.get_form(),
            "title": query,
        }
        return TemplateResponse(
            request,
            "weather/forecast.html",
            context=context
        )

    def post(self, request, *args, **kwargs):
        return send_search_request(
            self, request, *args, **kwargs
        )


def send_search_request(obj, request, *args, **kwargs):
    form = obj.get_form()
    context = {}
    if form.is_valid():
        query = form.cleaned_data['search_field']
        encoded_string = urllib.parse.quote(query)
        return redirect(
            reverse(
                "weather:detail",
                kwargs={"city": encoded_string}
            )
        )
    return TemplateResponse(request, reverse("weather:index"), context=context)
