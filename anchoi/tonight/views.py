from django.conf import settings
from django.db.models.expressions import OrderBy, RawSQL
from django.utils.dateparse import parse_datetime
from django.views.generic import DetailView, ListView

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
        context['active_city'] = self.kwargs.get('city')
        context['active_time'] = self.kwargs.get('time')
        return context
