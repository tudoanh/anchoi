from django.utils.dateparse import parse_datetime

from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
import django_filters
from rest_framework.filters import OrderingFilter

import facebook_bot


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def put(self, request, *args, **kwargs):
        event = self.queryset.filter(pk=kwargs['pk'])[0]
        if request.data.get('fb_id') != event.fb_id:
            return Response(
                data={'msg': 'Can not change facebook event\'s id'},
                status=status.HTTP_400_BAD_REQUEST
            )
        elif not request.data.get('name'):
            return Response(
                data={'msg': 'Name can not be emty'},
                status=status.HTTP_400_BAD_REQUEST
            )
        elif request.data.get('data') == event.data:
            return Response(
                data={'msg': 'Nothing changed'},
                status=status.HTTP_304_NOT_MODIFIED
            )
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_204_NO_CONTENT
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventFilter(filters.FilterSet):
    name = django_filters.CharFilter(name="name", lookup_expr=['search'])
    since = django_filters.DateFromToRangeFilter(
        name="start_time",
        label='Since',
    )

    order = django_filters.OrderingFilter(
        fields=(
            ("name", "name"),
            ("start_time", "time"),
        ),
        field_labels={
            'name': "Event name",
            'start_time': "Event start time"
        }
    )

    class Meta:
        model = Event
        fields = ['name', 'since']


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EventFilter

    # def get_queryset(self):
    #     queryset = Event.objects.all()
    #     base_time = self.request.query_params.get('since')
    #     latitude = self.request.query_params.get('latitude')
    #     longitude = self.request.query_params.get('longitude')
    #     if base_time:
    #         queryset = queryset.filter(
    #             start_time__gte=extract_datetime(base_time)
    #         )
    #     return queryset

    def create(self, request, *args, **kwargs):
        rq_data = request.data
        fb_id = rq_data.get('fb_id')
        if fb_id:
            fb_event = facebook_bot.get_event_info(fb_id)[fb_id]
            if fb_event:
                place = fb_event.get('place')
                location = place.get('location')
                event = {
                    'name': fb_event['name'],
                    'data': fb_event,
                    'fb_id': fb_id,
                    'start_time': parse_datetime(fb_event.get('start_time')),
                    'latitude': (
                        location.get('latitude') if place else ""
                    ),
                    'longitude': (
                        location.get('longitude') if place else ""
                    ),
                }
                serializer = EventSerializer(data=event)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        serializer.data,
                        status=status.HTTP_201_CREATED
                    )
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                data={'msg': 'Invalid facebook event ID'},
                status=status.HTTP_400_BAD_REQUEST
            )
        elif rq_data.get('data'):
            fb_event = rq_data.get('data')
            place = fb_event.get('place')
            location = place.get('location')
            event = {
                'name': fb_event['name'],
                'data': fb_event,
                'fb_id': fb_event['id'],
                'start_time': parse_datetime(fb_event.get('start_time')),
                'latitude': (
                    location.get('latitude') if place else ""
                ),
                'longitude': (
                    location.get('longitude') if place else ""
                ),
            }
            serializer = EventSerializer(data=event)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
