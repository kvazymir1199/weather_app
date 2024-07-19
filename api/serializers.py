from rest_framework import serializers
from weather.models import CityData


class CityRequestSerializer(serializers.ModelSerializer):
    requests = serializers.SerializerMethodField()

    def get_requests(self, obj):
        return obj.weather.count()

    class Meta:
        model = CityData
        fields = ("name", "slug", "requests")
