from django.conf import settings
from django.core.mail import send_mail
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector
)
from django.db.models.expressions import OrderBy, RawSQL
from django.http import HttpResponseRedirect
from django.utils.dateparse import parse_datetime
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from mailchimp3 import MailChimp

from events.models import Event
from events.utils import categories

from .forms import EmailForm, ContactForm
from .utils import cities, date_rage, queryset_for


URL = (
    'https://maps.googleapis.com/maps/api/staticmap?zoom=17&maptype=roadmap'
    '&markers=icon:https://i.imgur.com/MKelSUu.png|'
    '{0},{1}&size=600x600&key={2}'
)

API_KEY = settings.GOOGLE_API_KEY

MAILCHIMP_USER = settings.MAILCHIMP_USER
MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY


class TextContactView(FormView):
    template_name = 'text/contact.html'
    form_class = ContactForm
    success_url = '/success/'

    def form_valid(self, form):
        data = form.cleaned_data
        send_mail(
            data['subject'],
            data['body'],
            data['email'],
            ['admin@anchoi.today', ]
        )
        return super(TextContactView, self).form_valid(form)


class TextSubscribeView(FormView):
    template_name = 'text/subscribe.html'
    form_class = EmailForm
    success_url = '/thanks/'
    client = MailChimp(MAILCHIMP_USER, MAILCHIMP_API_KEY)

    def subscribe(self, list_id, email):
        self.client.lists.members.create(
            list_id,
            {
                'email_address': email,
                'status': 'subscribed',
            }
        )

    def form_valid(self, form):
        # https://github.com/charlesthk/python-mailchimp
        data = form.cleaned_data

        try:
            if data['city'] == 'ALL':
                self.subscribe('9219e7e784', data['email'])
            elif data['city'] == 'HN':
                self.subscribe('ebb54415a6', data['email'])
            elif data['city'] == 'SG':
                self.subscribe('ca0033027c', data['email'])
        except Exception:
            return HttpResponseRedirect('/subscribe/existed/')

        return super(TextSubscribeView, self).form_valid(form)


class TextEventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'text/event_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TextEventDetailView, self).get_context_data(**kwargs)
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


class TextSearchView(ListView):
    model = Event
    context_object_name = 'results'
    template_name = 'text/search.html'
    paginate_by = 12

    def get_queryset(self):
        result = super(TextSearchView, self).get_queryset()

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
        context = super(TextSearchView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class TextHomeView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'text/index.html'

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
        context = super(TextHomeView, self).get_context_data(**kwargs)
        context['hot'] = self.qs[:6]
        context['movie'] = self.qs.filter(queryset_for('movie'))[:6]
        context['music'] = self.qs.filter(queryset_for('music'))[:6]
        context['sport'] = self.qs.filter(queryset_for('sport'))[:6]
        context['education'] = self.qs.filter(queryset_for('education'))[:6]
        context['experience'] = self.qs.filter(queryset_for('experience'))[:6]
        context['active_city'] = self.kwargs.get('city', 'hanoi')
        context['active_time'] = 'week'
        return context


class TextEventByTimeView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'text/index.html'

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
        context = super(TextEventByTimeView, self).get_context_data(**kwargs)
        context['hot'] = self.qs[:6]
        context['movie'] = self.qs.filter(queryset_for('movie'))[:6]
        context['music'] = self.qs.filter(queryset_for('music'))[:6]
        context['sport'] = self.qs.filter(queryset_for('sport'))[:6]
        context['education'] = self.qs.filter(queryset_for('education'))[:6]
        context['experience'] = self.qs.filter(queryset_for('experience'))[:6]
        context['active_time'] = self.kwargs.get('time', 'week')
        context['active_city'] = self.kwargs.get('city', 'hanoi')
        return context


class TextEventByCategoryView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'text/event_by_category.html'

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
        context = super(
            TextEventByCategoryView,
            self
        ).get_context_data(**kwargs)
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
