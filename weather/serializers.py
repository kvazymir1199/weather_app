from rest_framework import serializers


class CitySerializer(serializers.Serializer):
    latitude = serializers.DecimalField(max_digits=10, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=10, decimal_places=6)
    timezone = serializers.CharField(max_length=256)
