from django.conf.urls import url
from django.views.generic.base import RedirectView, TemplateView

from .views import (
    TextEventByCategoryView,
    TextEventByTimeView,
    TextEventDetailView,
    TextHomeView,
    TextSearchView,
    TextSubscribeView,
    TextContactView
)


urlpatterns = [
    url(
        r'^$',
        RedirectView.as_view(url='/hanoi/')
    ),
    url(
        r'^contact/$',
        TextContactView.as_view(),
        name='text_contact_view'
    ),
    url(
        r'^success/$',
        TemplateView.as_view(template_name='text/success.html'),
        name='text_thanks_view'
    ),
    url(
        r'^subscribe/$',
        TextSubscribeView.as_view(),
        name='text_subscribe_view'
    ),
    url(
        r'^subscribe/existed/$',
        TemplateView.as_view(template_name='text/existed.html'),
        name='text_subscriber_existed_view'
    ),
    url(
        r'^thanks/$',
        TemplateView.as_view(template_name='text/thanks.html'),
        name='text_thanks_view'
    ),
    url(
        r'^search/$',
        TextSearchView.as_view(),
        name='text_search_view'
    ),
    url(
        r'^event/(?P<slug>[-\w]+)/$',
        TextEventDetailView.as_view(),
        name='text_event_detail_view'
    ),
    url(
        r'^(?P<city>[\w-]+)/$',
        TextHomeView.as_view(),
        name='text_home_view'
    ),
    url(
        r'^(?P<city>[\w-]+)/(?P<time>[\w-]+)/$',
        TextEventByTimeView.as_view(),
        name='text_event_by_time_view'
    ),
    url(
        r'^(?P<city>[\w-]+)/(?P<time>[\w-]+)/(?P<category>[\w-]+)/$',
        TextEventByCategoryView.as_view(),
        name='text_event_by_category_view'
    ),
]
