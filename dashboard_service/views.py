from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from dashboard_service.filters import BookingEventFilter
from dashboard_service.models import BookingEvent
from dashboard_service.serializers import DashboardApiSerializer
from dashboard_service.services import send_bookings
from dashboard_service.tasks import get_data_provider_events


class DashboardApiView(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    queryset = BookingEvent.objects.all().order_by("timestamp")
    serializer_class = DashboardApiSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookingEventFilter


class SendBookingApiView(viewsets.ViewSet):

    def create(self, request):
        try:
            send_bookings()

            return Response({"status": "ok"})
        except Exception as e:
            return Response({"status": "error", "message": str(e)})


class ViewBookingApiView(viewsets.ViewSet):

    def list(self, request):
        try:
            get_data_provider_events()

            return Response({"status": "ok"})
        except Exception as e:
            return Response({"status": "error", "message": str(e)})


