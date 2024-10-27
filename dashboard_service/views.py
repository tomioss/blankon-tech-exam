from rest_framework import viewsets
from rest_framework.response import Response

from dashboard_service.serializers import DashboardApiSerializer
from dashboard_service.services import send_bookings


class DashboardApiView(viewsets.ViewSet):

    def list(self, request):
        num_of_bookings = 0

        serializer = DashboardApiSerializer({"num_of_bookings": num_of_bookings})

        return Response(serializer.data)


class SendBookingApiView(viewsets.ViewSet):

    def create(self, request):
        try:
            send_bookings()

            return Response({"status": "ok"})
        except Exception as e:
            return Response({"status": "error", "message": str(e)})


