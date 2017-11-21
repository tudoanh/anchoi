from django.conf.urls import url
from django.views.generic.base import RedirectView, TemplateView

from .views import (
    EventByCategoryView,
    EventByTimeView,
    EventDetailView,
    HomeView,
    SearchView,
    SubscribeView,
    NearbyView,
)


urlpatterns = [
    url(
        r'^$',
        RedirectView.as_view(url='/hanoi/')
    ),
    url(
        r'^subscribe/$',
        SubscribeView.as_view(),
        name='subscribe_view'
    ),
    url(
        r'^subscribe/existed/$',
        TemplateView.as_view(template_name='tonight/existed.html'),
        name='subscriber_existed_view'
    ),
    url(
        r'^thanks/$',
        TemplateView.as_view(template_name='tonight/thanks.html'),
        name='thanks_view'
    ),
    url(
        r'^search/$',
        SearchView.as_view(),
        name='search_view'
    ),
    url(
        r'^nearby/$',
        NearbyView.as_view(),
        name='nearby_view'
    ),
    url(
        r'^event/(?P<slug>[-\w]+)/$',
        EventDetailView.as_view(),
        name='event_detail_view'
    ),
    url(
        r'^(?P<city>[\w-]+)/$',
        HomeView.as_view(),
        name='home_view'
    ),
    url(
        r'^(?P<city>[\w-]+)/(?P<time>[\w-]+)/$',
        EventByTimeView.as_view(),
        name='event_by_time_view'
    ),
    url(
        r'^(?P<city>[\w-]+)/(?P<time>[\w-]+)/(?P<category>[\w-]+)/$',
        EventByCategoryView.as_view(),
        name='event_by_category_view'
    ),
]
