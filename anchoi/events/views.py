from django.utils.dateparse import parse_datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Event
from .serializers import EventSerializer
from .utils import extract_datetime
from rest_framework import generics

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


@api_view(['GET', 'POST'])
def get_post_events(requests):
    if requests.method == 'GET':
        if requests.query_params.get('since'):
            base_time = requests.query_params.get('since')
            queryset = Event.objects.filter(
                start_time__gte=extract_datetime(base_time)
            )
            paginator = PageNumberPagination()
            events_since = paginator.paginate_queryset(queryset, requests)
            serializer = EventSerializer(
                events_since,
                many=True,
                context={'requests': requests}
            )
            return paginator.get_paginated_response(serializer.data)
        queryset = Event.objects.all()
        paginator = PageNumberPagination()
        events = paginator.paginate_queryset(queryset, requests)
        serializer = EventSerializer(
            events,
            many=True,
            context={'requests': requests}
        )
        return paginator.get_paginated_response(serializer.data)
    elif requests.method == 'POST':
        rq_data = requests.data
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
