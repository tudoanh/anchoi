import operator
from functools import reduce


from django.db.models import Q
from django.db.utils import IntegrityError
from django.db.models.expressions import RawSQL, OrderBy
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

import django_filters
import facebook_bot

from .models import Event
from .serializers import EventSerializer
from . utils import extract_event_data, categories



class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
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


class CustomOrderingFilter(django_filters.OrderingFilter):
    def __init__(self, *args, **kwargs):
        super(CustomOrderingFilter, self).__init__(*args, **kwargs)
        self.extra['choices'] += [
            ('attending_count', 'Attending'),
        ]

    def filter(self, qs, value):
        if any(v in ['attending_count', ] for v in value):
            return qs.order_by(OrderBy(RawSQL(
                "cast(data->>%s as integer)",
                ('attending_count',)),
                descending=True)
            )

        return super(CustomOrderingFilter, self).filter(qs, value)


class EventFilter(filters.FilterSet):
    name = django_filters.CharFilter(name="name", lookup_expr=['search'])
    category = django_filters.CharFilter(
        label='Category',
        name="name",
        method='filter_by_category'
    )
    city = django_filters.CharFilter(
        name='data__place__location__city',
        label='City'
    )
    since = django_filters.DateFromToRangeFilter(
        name="start_time",
        label='Since',
    )

    order = CustomOrderingFilter(
        fields=(
            ("name", "name"),
            ("start_time", "time"),
        ),
        field_labels={
            'name': "Event name",
            'start_time': "Event start time",
        }
    )

    def filter_by_category(self, queryset, name, value):
        query = reduce(
            operator.or_,
            (Q(name__icontains=keyword)
                for keyword in categories.get(value, []))
        )
        return queryset.filter(query)

    class Meta:
        model = Event
        fields = ['name', 'since', 'city', 'category']


class EventList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EventFilter

    def create(self, request, *args, **kwargs):
        rq_data = request.data
        fb_id = rq_data.get('fb_id')
        try:
            if fb_id:
                fb_event = facebook_bot.get_event_info(fb_id)[fb_id]
                if fb_event:
                    event = extract_event_data(fb_event)
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
                event = extract_event_data(fb_event)
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
        except IntegrityError:
            return Response(
                {'msg': 'Event is existed.'},
                status=status.HTTP_409_CONFLICT
            )
