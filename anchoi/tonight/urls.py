from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
    EventByCategoryView,
    EventByTimeView,
    EventDetailView,
    HomeView,
    SearchView,
)


urlpatterns = [
    url(
        r'^$',
        RedirectView.as_view(url='/hanoi/')
    ),
    url(
        r'^search/$',
        SearchView.as_view(),
        name='search_view'
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
