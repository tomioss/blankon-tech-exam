from django.contrib import admin

from .models import BookingEvent


class BookingEventAdmin(admin.ModelAdmin):
    model = BookingEvent
    list_display = (
        "id",
        "booking_id",
        "hotel_id",
        "room_id",
        "rpg_status",
        "night_of_stay",
        "timestamp",
        "created_at",
        "updated_at",
    )


admin.site.register(BookingEvent, BookingEventAdmin)

