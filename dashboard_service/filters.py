from django_filters import rest_framework as filters

from dashboard_service.models import BookingEvent


class BookingEventFilter(filters.FilterSet):
    month = filters.NumberFilter(field_name="night_of_stay", lookup_expr="month")
    day = filters.NumberFilter(field_name="night_of_stay", lookup_expr="day")
    year = filters.NumberFilter(field_name="night_of_stay", lookup_expr="year")

    class Meta:
        model = BookingEvent
        fields = (
            "hotel_id",
        )

