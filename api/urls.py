from django.urls import path
from .views import RequestsCountView, RequestsListCountView

urlpatterns = [
    path("", RequestsListCountView.as_view()),
    path("<str:slug>", RequestsCountView.as_view())
]
