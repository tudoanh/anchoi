import json
from rest_framework import status
from django.test import TestCase, TransactionTestCase
from django.urls import reverse
from ..models import Event
from ..serializers import EventSerializer
from .mockdata import events_data
from rest_framework.test import APIClient
from django.contrib.auth.models import User


guest = APIClient()
client = APIClient()


class GetAllEventsTest(TestCase):
    """
    Test module for GET all events API
    """

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
        Event.objects.create(
            name='John Jay College Family Palooza 2017',
            data=events_data['event3'],
            fb_id='1446325218750262',
        )
        Event.objects.create(
            name='Smart On Crime Innovations Conference',
            data=events_data['event4'],
            fb_id='1936389863288565'
        )
        Event.objects.create(
            name='Fridays Under 40: The Exterminating Angel',
            data=events_data['event5'],
            fb_id='129926020973198',
        )
        Event.objects.create(
            name='PMT FALL DANCE SERIES at Manhattan Movement and Arts Center',
            data=events_data['event6'],
            fb_id='352165395207352'
        )

    def test_get_all_events(self):
        response = client.get(reverse('get_post_events'))
        events = Event.objects.all()
        serializers = EventSerializer(events, many=True)
        self.assertEqual(response.data['results'], serializers.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetEventByNameTest(TestCase):
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
        Event.objects.create(
            name='Sugar Factory UWS Family Mixer.',
            data=events_data['event7'],
            fb_id='108842849758568'
        )

    def test_get_event_by_name(self):
        response = client.get(
            reverse('get_post_events'),
            data={'name_0': '21', 'name_1': 'search'},
            content_type='application/json'
        )
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetEventsByCategory(TestCase):  # TODO
    pass


class GetEventsByDateTimeTest(TestCase):
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
        Event.objects.create(
            name='Sugar Factory UWS Family Mixer.',
            data=events_data['event7'],
            fb_id='108842849758568'
        )

    def test_get_valid_date_time(self):
        response = client.get(
            reverse('get_post_events'),
            data={'since_0': '2017-10-09'},
            content_type='application/json'
        )
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleEventTest(TestCase):
    def setUp(self):
        self.event1 = Event.objects.create(
            name='21 West End Halloween Party',
            data=events_data['event1'],
            fb_id='363481930775199',
        )
        self.event2 = Event.objects.create(
            name='Sunday Brunch at Cafe 21',
            data=events_data['event2'],
            fb_id='1292167920892181'
        )

    def test_get_valid_single_event(self):
        response = client.get(
            reverse('get_delete_put_event', kwargs={'pk': self.event1.pk})
        )
        event = Event.objects.get(pk=self.event1.pk)
        serializers = EventSerializer(event)
        self.assertEqual(response.data, serializers.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_event(self):
        response = client.get(
            reverse('get_delete_put_event', kwargs={'pk': 50})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewEventTest(TransactionTestCase):
    def setUp(self):
        self.valid_payload = {
            'name': '',
            'data': events_data['event1'],
            'fb_id': ''
        }

        self.valid_payload_2 = {
            'name': '',
            'data': '',
            'fb_id': '363481930775199'
        }

        self.no_location_payload = {
            'name': '',
            'data': events_data['event8'],
            'fb_id': ''
        }

        self.invalid_payload = {
            'name': '',
            'data': '',
            'fb_id': ''
        }

        self.admin = APIClient()
        self.admin_acc = User.objects.create_superuser(
            username='demoadmin',
            password='thisisaadminpassword123',
            email='abc@example.com'
        )
        self.admin.force_authenticate(user=self.admin_acc)

    def tearDown(self):
        self.admin_acc.delete()

    def test_create_valid_event(self):
        response = self.admin.post(
            reverse('get_post_events'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_no_location_event(self):
        response = self.admin.post(
            reverse('get_post_events'),
            data=json.dumps(self.no_location_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_valid_event_with_fb_id(self):
        response = self.admin.post(
            reverse('get_post_events'),
            data=json.dumps(self.valid_payload_2),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_event(self):
        response = self.admin.post(
            reverse('get_post_events'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_event_is_exist(self):
        self.admin.post(
            reverse('get_post_events'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        response = self.admin.post(
            reverse('get_post_events'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.data, {'msg': 'Event is existed.'})
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_guest_can_not_create_event(self):
        response = guest.post(
            reverse('get_post_events'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UpdateSingleEventTest(TestCase):
    def setUp(self):
        self.event1 = Event.objects.create(
            name='21 West End Halloween Party',
            data=events_data['event1'],
            fb_id='363481930775199',
        )

        self.valid_payload = {
            'name': '21 West End Halloween Party',
            'data': events_data['changed_event_1'],
            'fb_id': '363481930775199',
        }
        self.invalid_name_payload = {
            'name': '',
            'data': events_data['changed_event_1'],
            'fb_id': '363481930775199'
        }
        self.invalid_fb_id_payload = {
            'name': '21 West End Halloween Party',
            'data': events_data['changed_event_1'],
            'fb_id': '123123123',
        }
        self.nothing_changed_payload = {
            'name': '21 West End Halloween Party',
            'data': events_data['event1'],
            'fb_id': '363481930775199',
        }
        self.admin = APIClient()
        self.admin_acc = User.objects.create_superuser(
            username='demoadmin',
            password='thisisaadminpassword123',
            email='abc@example.com'
        )
        self.admin.force_authenticate(user=self.admin_acc)

    def tearDown(self):
        self.admin_acc.delete()

    def test_valid_update_event(self):
        response = self.admin.put(
            reverse('get_delete_put_event', kwargs={'pk': self.event1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_name_update_event(self):
        response = self.admin.put(
            reverse('get_delete_put_event', kwargs={'pk': self.event1.pk}),
            data=json.dumps(self.invalid_name_payload),
            content_type='application/json'
        )
        self.assertEqual(response.data, {'msg': 'Name can not be emty'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_fb_id_payload(self):
        response = self.admin.put(
            reverse('get_delete_put_event', kwargs={'pk': self.event1.pk}),
            data=json.dumps(self.invalid_fb_id_payload),
            content_type='application/json'
        )
        self.assertEqual(
            response.data,
            {'msg': 'Can not change facebook event\'s id'}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_nothing_changed_payload(self):
        response = self.admin.put(
            reverse('get_delete_put_event', kwargs={'pk': self.event1.pk}),
            data=json.dumps(self.nothing_changed_payload),
            content_type='application/json'
        )
        self.assertEqual(response.data, {'msg': 'Nothing changed'})
        self.assertEqual(response.status_code, status.HTTP_304_NOT_MODIFIED)

    def test_guest_can_not_change_event(self):
        response = guest.put(
            reverse('get_delete_put_event', kwargs={'pk': self.event1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class DeleteSingleEventTest(TestCase):
    def setUp(self):
        self.event1 = Event.objects.create(
            name='21 West End Halloween Party',
            data=events_data['event1'],
            fb_id='363481930775199',
        )
        self.admin = APIClient()
        self.admin_acc = User.objects.create_superuser(
            username='demoadmin',
            password='thisisaadminpassword123',
            email='abc@example.com'
        )
        self.admin.force_authenticate(user=self.admin_acc)

    def tearDown(self):
        self.admin_acc.delete()

    def test_valid_delete_event(self):
        response = self.admin.delete(
            reverse('get_delete_put_event', kwargs={'pk': self.event1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_event(self):
        response = self.admin.delete(
            reverse('get_delete_put_event', kwargs={'pk': 30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_guest_can_not_delete_event(self):
        response = guest.delete(
            reverse('get_delete_put_event', kwargs={'pk': self.event1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
