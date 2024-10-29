# blankon-tech-exam

### Installation
Run `docker compose up`  
Run `docker compose run --rm backend python manage.py migrate`  

### API Endpoints
POST and GET localhost:8000/events/  
GET localhost:8000/dashboard/

Reads the `data.csv` and calls the POST Events API  
POST localhost:8000/send_booking/

Manual Trigger API of the periodic task that checks for new bookings and saves to dashboard service's table  
GET localhost:8000/view_booking/

### Periodic Tasks
Calls the POST Events API daily to simulate sending of new data  
save_data_provider_events

Checks for new bookings for the day and saves to dashboard service's table
get_data_provider_events


### Testing
Run `docker compose run --rm backend python manage.py test`

### Commands
```
docker compose up
docker compose run --rm backend python manage.py shell
docker compose run --rm backend python manage.py test --keepdb
```

### Local Testing
```
crontab(minute='*/1')
```

