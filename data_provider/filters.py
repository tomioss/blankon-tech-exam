from django_filters import rest_framework as filters

from data_provider.models import Event


class EventFilter(filters.FilterSet):
    updated_gte = filters.DateTimeFilter(field_name="timestamp", lookup_expr="gte")
    updated_lte = filters.DateTimeFilter(field_name="timestamp", lookup_expr="lte")
    night_of_stay_gte = filters.DateFilter(field_name="night_of_stay", lookup_expr="gte")
    night_of_stay_lte = filters.DateFilter(field_name="night_of_stay", lookup_expr="lte")

    class Meta:
        model = Event
        fields = (
            "hotel_id",
            "rpg_status",
            "room_id",
        )

