from django.db import models


class Event(models.Model):
    hotel_id = models.IntegerField()
    room_reservation_id = models.UUIDField()
    room_id = models.IntegerField()
    rpg_status = models.IntegerField()
    night_of_stay = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

