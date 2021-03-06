from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    data = serializers.JSONField()
    fb_id = serializers.CharField()
    start_time = serializers.DateTimeField()
    latitude = serializers.CharField(allow_blank=True)
    longitude = serializers.CharField(allow_blank=True)

    class Meta:
        model = Event
        fields = (
            'name', 'data', 'fb_id', 'start_time', 'latitude', 'longitude'
        )
