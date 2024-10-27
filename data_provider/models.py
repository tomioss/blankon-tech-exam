from django.db import models


class Event(models.Model):
    booking_id = models.IntegerField()
    hotel_id = models.IntegerField()
    room_id = models.CharField(max_length=60)
    rpg_status = models.IntegerField()
    night_of_stay = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

