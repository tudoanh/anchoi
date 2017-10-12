from datetime import datetime
import pytz
from django.utils.dateparse import parse_datetime


def extract_datetime(date_str):
    timezone = 'Asia/Saigon'
    return pytz.timezone(timezone).localize(
        datetime.strptime(date_str, "%Y-%m-%d")
    )


def extract_event_data(fb_event):
    place = fb_event.get('place')
    location = place.get('location')
    event = {
        'name': fb_event['name'],
        'data': fb_event,
        'fb_id': fb_event['id'],
        'start_time': parse_datetime(
            fb_event.get('start_time')
        ),
        'latitude': (
            location.get('latitude') if place and location else None
        ),
        'longitude': (
            location.get('longitude') if place and location else None
        ),
    }
    return event
