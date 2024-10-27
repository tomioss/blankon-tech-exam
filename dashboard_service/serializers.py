from rest_framework import serializers

from dashboard_service.models import BookingEvent


class DashboardApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingEvent
        fields = (
            "booking_id",
            "hotel_id",
            "timestamp",
            "rpg_status",
            "room_id",
            "night_of_stay",
        )

