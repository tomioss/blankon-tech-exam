from django_filters import rest_framework as filters

from dashboard_service.models import BookingEvent


class BookingEventFilter(filters.FilterSet):

    class Meta:
        model = BookingEvent
        fields = (
            "hotel_id",
        )

