"""
Create your tasks here.

Tasks will be queue to Celery
"""
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import facebook_bot as bot

from .coorcal import generate_coordinate
from .models import Event, FacebookPage
from .serializers import EventSerializer
from .utils import extract_event_data

from anchoi.utils import send_msg


@shared_task
def hourly_scan():
    """
    Scan every events in db, if event does not exists, delete it.
    """

    for event in Event.objects.all():
        e = bot.get_event_info(event.fb_id)
        if e:
            try:
                node = e[event.fb_id]
                if event.data == node:
                    pass
                else:
                    data = extract_event_data(node)
                    serializer = EventSerializer(
                        event,
                        data=data,
                        partial=True
                    )
                    if serializer.is_valid():
                        serializer.save()
            except Exception as e:
                send_msg(e)
                pass
        else:
            event.delete()


@shared_task
def daily_scan():
    """
    Scan all Page in db, if have any new events, create it.
    """

    for page in FacebookPage.objects.all():
        if bot.get_events(page.page_id):
            try:
                res = list(bot.get_events(page.page_id).values())[0]
                if res.get('events'):
                    for event in res['events']['data']:
                        if Event.objects.filter(fb_id=event['id']):
                            pass
                        else:
                            data = extract_event_data(event)
                            serializer = EventSerializer(data=data)
                            if serializer.is_valid():
                                serializer.save()
            except Exception:
                pass
        else:
            page.delete()


@shared_task
def weekly_page_scan(lat, lon, distance, scan_radius=200):
    circle = (lat, lon, distance, )
    for point in generate_coordinate(*circle, scan_radius=scan_radius):
        page_list = bot.get_page_ids(
            latitude=point[0],
            longitude=point[1],
            query_agrument='*',
            distance=scan_radius)
        for page_id in page_list:
            FacebookPage.objects.get_or_create(
                page_id=page_id
            )
