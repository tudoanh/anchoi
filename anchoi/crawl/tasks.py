import facebook_bot as fb
import requests

from events.models import FacebookPage, Event
from events.utils import extract_event_data


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


def save_page_info(event):
    info = event['owner']
    return FacebookPage.objects.get_or_create(
        name=info['name'],
        page_id=info['id']
    )


def update_event(event_id, data):
    requests.put(
        UPDATE_EVENT_URL.format(event_id),
        json={
            'name': data['name'],
            'fb_id': data['id'],
            'data': data
        },
        auth=(USERNAME, PASSWORD)
    )


def create_event(data):
    for e in data:
        requests.post(
            CREATE_EVENT_URL,
            auth=(USERNAME, PASSWORD),
            json={'data': e}
        )


def weekly_scan(lat, lon, dis):
    for data in fb.get_events_by_location(lat, lon, dis, fields=EVENT_FIELDS):
        save_page_info(data[0])
        create_event(data)


def daily_scan():
    for page in FacebookPage.objects.all():
        res = list(fb.get_events(page.page_id).values())[0]
        if res.get('events'):
            create_event(res['events']['data'])


def hourly_scan():
    for event in Event.objects.all():
        try:
            e = fb.get_event_info(event.fb_id)[event.fb_id]
        except Exception:
            pass
        update_event(event.id, e)
