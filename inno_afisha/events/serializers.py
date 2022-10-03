from rest_framework import serializers

from events.models import EventModel


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = "__all__"