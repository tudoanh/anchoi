from django.test import TestCase
from ..models import Event
from .mockdata import events_data


class EventTest(TestCase):
    """Test module for Event model"""
    def setUp(self):
        Event.objects.create(
            name='21 West End Halloween Party',
            data=events_data['event1'],
            fb_id='363481930775199',
        )
        Event.objects.create(
            name='Sunday Brunch at Cafe 21',
            data=events_data['event2'],
            fb_id='1292167920892181'
        )

    def test_event_info(self):
        event_1 = Event.objects.get(name='21 West End Halloween Party')
        event_2 = Event.objects.get(name='Sunday Brunch at Cafe 21')
        self.assertEqual(
            event_1.data['id'], '363481930775199'
        )
        self.assertEqual(
            event_2.data['id'], '1292167920892181'
        )
