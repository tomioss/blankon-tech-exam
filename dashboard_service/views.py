from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dashboard_service.filters import BookingEventFilter
from dashboard_service.models import BookingEvent
from dashboard_service.serializers import DashboardApiSerializer
from dashboard_service.services import get_data_provider_and_save_events, send_bookings
from dashboard_service.utils import get_date_time_today


class DashboardApiView(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = BookingEvent.objects.all().order_by("timestamp")
    serializer_class = DashboardApiSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookingEventFilter


class SendBookingApiView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        try:
            hotel_id = request.GET.get("hotel_id", None)
            room_reservation_id = request.GET.get("room_reservation_id", None)

            params = {}
            if hotel_id:
                params["hotel_id"] = hotel_id
            if room_reservation_id:
                params["room_reservation_id"] = room_reservation_id

            if not params:
                send_bookings()
            else:
                send_bookings(params)

            return Response({"status": "ok"})
        except Exception as e:
            return Response({"status": "error", "message": str(e)})


class ViewBookingApiView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        try:
            default_start_time, default_end_time = get_date_time_today()
            start_time = request.GET.get("start_time", default_start_time)
            end_time = request.GET.get("end_time", default_end_time)

            get_data_provider_and_save_events(start_time, end_time)

            return Response({"status": "ok"})
        except Exception as e:
            return Response({"status": "error", "message": str(e)})


