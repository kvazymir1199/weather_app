from rest_framework import serializers
from .models import CityData


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityData
        fields = "__all__"
