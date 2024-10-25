from rest_framework import serializers

class DashboardApiSerializer(serializers.Serializer):
    num_of_bookings = serializers.IntegerField()

