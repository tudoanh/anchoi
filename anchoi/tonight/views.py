from datetime import datetime

from django.views.generic import ListView
from django.db.models.expressions import RawSQL, OrderBy

from events.models import Event
from events.views import EventFilter

from .utils import generate_date_range, date_rage, queryset_for, cities


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
                    self.kwargs.get('city'), ''
                )
            )
            .filter(
                start_time__range=date_rage.get('month')
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
        return context


class EventByTimeView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'tonight/event_by_time.html'

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
                    self.kwargs.get('time', 'today')
                )
            )
            .order_by(OrderBy(RawSQL(
                "cast(data->>%s as integer)",
                ('attending_count',)),
                descending=True)
            )
        )

        return self.qs


class EventByCategoryView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'tonight/event_by_category.html'

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
                    self.kwargs.get('time', 'today')
                )
            )
            .filter(
                queryset_for(self.kwargs.get('category', ''))
            )
            .order_by(OrderBy(RawSQL(
                "cast(data->>%s as integer)",
                ('attending_count',)),
                descending=True)
            )
        )

        return self.qs
