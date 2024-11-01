from rest_framework import serializers

from data_provider.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            "booking_id",
            "hotel_id",
            "timestamp",
            "rpg_status",
            "room_id",
            "night_of_stay",
        )


class EventCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"

