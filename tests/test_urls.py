from django.test import TestCase, Client
from django.urls import reverse
from django import forms

from weather.forms import SearchForm
from weather.models import WeatherData


class StaticURLTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_page_exists(self):
        response = self.client.get(reverse("weather:index"))
        self.assertEqual(response.status_code, 200)

    def test_main_page_use_correct_template(self):
        response = self.client.get(reverse("weather:index"))
        self.assertTemplateUsed(response, 'weather/index.html')

    def test_detail_page_exists(self):
        response = self.client.get(reverse("weather:detail", kwargs={"city": "berlin"}))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_use_correct_template(self):
        response = self.client.get(reverse("weather:detail", kwargs={"city": "berlin"}))
        self.assertTemplateUsed(response, 'weather/forecast.html')

    def test_main_page_correct_context(self):
        response = self.client.get(reverse("weather:index"))
        form_fields = {
            'search_field': forms.fields.CharField,
        }
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get('form').fields.get(value)
                self.assertIsInstance(form_field, expected)

    def test_detail_page_correct_context(self):
        response = self.client.get(reverse("weather:detail", kwargs={"city": "berlin"}))
        form = response.context["form"]
        title = response.context["title"]
        self.assertIsInstance(form, SearchForm)
        self.assertEqual(title, "berlin")
