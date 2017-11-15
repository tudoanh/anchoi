# coding=utf-8

"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""

from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector
)
from django.db.models.expressions import OrderBy, RawSQL
from django.utils.dateparse import parse_datetime
from django.views.generic import DetailView, ListView, TemplateView

from events.models import Event
from events.utils import categories

from .utils import cities, date_rage, queryset_for


URL = (
    'https://maps.googleapis.com/maps/api/staticmap?zoom=17&maptype=roadmap'
    '&markers=icon:https://i.imgur.com/MKelSUu.png|'
    '{0},{1}&size=600x600&key={2}'
)

API_KEY = settings.GOOGLE_API_KEY


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'tonight/event_detail.html'

    def get_context_data(self, **kwargs):
        '''
        Context data
        '''

        context = super(EventDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        if obj.data.get('end_time'):
            context['end_time'] = parse_datetime(obj.data.get('end_time'))

        try:
            place = obj.data['place']
            context['place_name'] = place['name']
            context['city'] = place['location']['city']
            context['street'] = place['location']['street']
        except KeyError:
            pass

        context['map'] = URL.format(obj.latitude, obj.longitude, API_KEY)

        return context


class NearbyView(ListView):
    model = Event
    context_object_name = 'results'
    template_name = 'tonight/nearby.html'

    def get_queryset(self):
        result = super(NearbyView, self).get_queryset()

        self.qs = Event.objects.all()
        lat = self.request.GET.get('latitude')
        lng = self.request.GET.get('longitude')
        if lat and lng:
            geo = Point(float(lat), float(lng))
            distance = 500
            self.qs = (
                self.qs
                .filter(point__distance_lte=(geo, D(m=distance)))
                .distance(geo)
                .order_by('distance')
            )
            result = self.qs

        return result

    def get_context_data(self, **kwargs):
        context = super(NearbyView, self).get_context_data(**kwargs)
        context['today'] = self.qs.filter(
            start_time__range=date_rage.get('today')
        )
        context['weekend'] = self.qs.filter(
            start_time__range=date_rage.get('weekend')
        )
        context['week'] = self.qs.filter(
            start_time__range=date_rage.get('week')
        )
        return context


class SearchView(ListView):
    model = Event
    context_object_name = 'results'
    template_name = 'tonight/search.html'
    paginate_by = 12

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            vector = (
                SearchVector('name', weight='A')
            )
            query = SearchQuery(query)
            result = (
                Event
                .objects
                .annotate(rank=SearchRank(vector, query))
                .filter(rank__gte=0.3)
                .order_by('rank')
            )

        return result

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class HomeView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'tonight/index.html'

    def get_queryset(self):
        self.qs = (
            Event
            .objects
            .filter(
                data__place__location__city=cities.get(
                    self.kwargs.get('city'), 'hanoi'
                )
            )
            .filter(
                start_time__range=date_rage.get('week')
            )
            .order_by(OrderBy(RawSQL(
                "cast(data->>%s as integer)",
                ('attending_count',)),
                descending=True)
            )
        )

        return self.qs

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['hot'] = self.qs[:6]
        context['movie'] = self.qs.filter(queryset_for('movie'))[:6]
        context['music'] = self.qs.filter(queryset_for('music'))[:6]
        context['sport'] = self.qs.filter(queryset_for('sport'))[:6]
        context['education'] = self.qs.filter(queryset_for('education'))[:6]
        context['experience'] = self.qs.filter(queryset_for('experience'))[:6]
        context['active_city'] = self.kwargs.get('city', 'hanoi')
        context['active_time'] = 'week'
        return context


class EventByTimeView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'tonight/index.html'

    def get_queryset(self):
        self.qs = (
            Event
            .objects
            .filter(
                data__place__location__city=cities.get(
                    self.kwargs.get('city', 'hanoi')
                )
            )
            .filter(
                start_time__range=date_rage.get(
                    (
                        'today'
                        if self.kwargs.get('time') not in date_rage
                        else self.kwargs.get('time')
                    )
                )
            )
            .order_by(OrderBy(RawSQL(
                "cast(data->>%s as integer)",
                ('attending_count',)),
                descending=True)
            )
        )

        return self.qs

    def get_context_data(self, **kwargs):
        context = super(EventByTimeView, self).get_context_data(**kwargs)
        context['hot'] = self.qs[:6]
        context['movie'] = self.qs.filter(queryset_for('movie'))[:6]
        context['music'] = self.qs.filter(queryset_for('music'))[:6]
        context['sport'] = self.qs.filter(queryset_for('sport'))[:6]
        context['education'] = self.qs.filter(queryset_for('education'))[:6]
        context['experience'] = self.qs.filter(queryset_for('experience'))[:6]
        context['active_time'] = self.kwargs.get('time', 'week')
        context['active_city'] = self.kwargs.get('city', 'hanoi')
        return context


class EventByCategoryView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'tonight/event_by_category.html'
    paginate_by = 12

    def get_queryset(self):
        self.qs = (
            Event
            .objects
            .filter(
                data__place__location__city=cities.get(
                    self.kwargs.get('city'), 'hanoi'
                )
            )
            .filter(
                start_time__range=date_rage.get(
                    (
                        'today'
                        if self.kwargs.get('time') not in date_rage
                        else self.kwargs.get('time')
                    )
                )
            )
            .filter(
                queryset_for(
                    (
                        ''
                        if self.kwargs.get('category') not in categories
                        else self.kwargs.get('category')
                    )
                )
            )
            .order_by(OrderBy(RawSQL(
                "cast(data->>%s as integer)",
                ('attending_count',)),
                descending=True)
            )
        )

        return self.qs

    def get_context_data(self, **kwargs):
        context = super(EventByCategoryView, self).get_context_data(**kwargs)
        category_title = {
            'movie': 'phim/điện ảnh',
            'music': 'âm nhạc',
            'experience': 'trải nghiệm',
            'education': 'giáo dục',
            'sport': 'thể thao'
        }
        time_title = {
            'today': 'hôm nay',
            'weekend': 'cuối tuần',
            'week': 'tuần này',
            'month': 'tháng này'
        }
        context['active_city'] = self.kwargs.get('city')
        context['active_time'] = time_title.get(self.kwargs.get('time'))
        context['active_category'] = category_title.get(
            self.kwargs.get('category'),
            ''
        )

        return context
