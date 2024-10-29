from datetime import datetime
from uuid import uuid4

from django.utils import timezone


def get_date_time_today():
    now = datetime.now()
    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end = now.replace(hour=23, minute=59, second=59, microsecond=59)
    return start, end

def get_booking_data():
    room_id_1 = str(uuid4())
    time_now = timezone.now()
    return [
        {
            "booking_id": 1,
            "hotel_id": 2607,
            "timestamp": time_now,
            "rpg_status": 1,
            "room_id": room_id_1,
            "night_of_stay": "2024-10-26"
        },
        {
            "booking_id": 2,
            "hotel_id": 2607,
            "timestamp": time_now,
            "rpg_status": 1,
            "room_id": room_id_1,
            "night_of_stay": "2024-10-27"
        },
        {
            "booking_id": 3,
            "hotel_id": 2607,
            "timestamp": time_now,
            "rpg_status": 1,
            "room_id": room_id_1,
            "night_of_stay": "2024-10-28"
        },
        {
            "booking_id": 4,
            "hotel_id": 2607,
            "timestamp": time_now,
            "rpg_status": 1,
            "room_id": room_id_1,
            "night_of_stay": "2024-10-29"
        },
        {
            "booking_id": 5,
            "hotel_id": 2607,
            "timestamp": time_now,
            "rpg_status": 1,
            "room_id": room_id_1,
            "night_of_stay": "2024-10-30"
        },
        {
            "booking_id": 6,
            "hotel_id": 2607,
            "timestamp": time_now,
            "rpg_status": 1,
            "room_id": str(uuid4()),
            "night_of_stay": "2024-10-29"
        },
        {
            "booking_id": 7,
            "hotel_id": 2607,
            "timestamp": time_now,
            "rpg_status": 1,
            "room_id": str(uuid4()),
            "night_of_stay": "2024-10-30"
        },
        {
            "booking_id": 8,
            "hotel_id": 2607,
            "timestamp": time_now,
            "rpg_status": 1,
            "room_id": str(uuid4()),
            "night_of_stay": "2024-10-31"
        },
    ]

