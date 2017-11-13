# from events.utils import extract_event_data
from events.models import Event, FacebookPage

import facebook_bot as fb

import requests

from .coorcal import generate_coordinate


HANOI_CENTER = (21.028811, 105.848977)
SAIGON_CENTER = (10.782812, 106.695886)

API_URL = 'http://localhost:8000/api/v1.0/'
CREATE_EVENT_URL = API_URL + 'events/'
UPDATE_EVENT_URL = API_URL + 'events/{}'
USERNAME = ''
PASSWORD = ''


EVENT_FIELDS = [
    'id',
    'name',
    'start_time',
    'end_time',
    'description',
    'place',
    'type',
    'category',
    'ticket_uri',
    'cover.fields(id,source)',
    'picture.type(large)',
    'attending_count',
    'declined_count',
    'maybe_count',
    'noreply_count',
    'owner'
]


def weekly_page_scan(lat, lon, distance, scan_radius=200):
    circle = (lat, lon, distance, )
    for point in generate_coordinate(*circle, scan_radius=scan_radius):
        page_list = fb.get_page_ids(
            latitude=point[0],
            longitude=point[1],
            query_agrument='*',
            distance=scan_radius)
        for page_id in page_list:
            FacebookPage.objects.get_or_create(
                page_id=page_id
            )


def daily_scan():
    for page in FacebookPage.objects.all():
        res = list(fb.get_events(page.page_id).values())[0]
        if res.get('events'):
            for event in res['events']['data']:
                requests.post(
                    CREATE_EVENT_URL,
                    auth=(USERNAME, PASSWORD),
                    json={'data': event}
                )


def hourly_scan():
    for event in Event.objects.all():
        try:
            e = fb.get_event_info(event.fb_id)[event.fb_id]
        except Exception:
            pass
        requests.put(
            UPDATE_EVENT_URL.format(event.id),
            json={
                'name': e['name'],
                'fb_id': e['id'],
                'data': e
            },
            auth=(USERNAME, PASSWORD)
        )
