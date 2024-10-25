from rest_framework import viewsets
from rest_framework.response import Response

from dashboard_service.serializers import DashboardApiSerializer

class DashboardApiView(viewsets.ViewSet):

    def list(self, request):
        num_of_bookings = 0

        serializer = DashboardApiSerializer({"num_of_bookings": num_of_bookings})

        return Response(serializer.data)

