from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (
    TextEventByCategoryView,
    TextEventByTimeView,
    TextEventDetailView,
    TextHomeView,
    TextSearchView,
)


urlpatterns = [
    url(
        r'^$',
        RedirectView.as_view(url='/hanoi/')
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
