from rest_framework.generics import RetrieveAPIView, ListAPIView
from weather.models import CityData
from .serializers import CityRequestSerializer


class RequestsListCountView(ListAPIView):
    queryset = CityData.objects.all()
    serializer_class = CityRequestSerializer


class RequestsCountView(RetrieveAPIView):
    queryset = CityData.objects.all()
    serializer_class = CityRequestSerializer
    lookup_field = "slug"
