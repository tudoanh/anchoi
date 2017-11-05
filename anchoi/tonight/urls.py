from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^$',
        views.HomeView.as_view(),
        name='home_view'
    ),
    url(
        r'^(?P<city>[\w-]+)/$',
        views.HomeView.as_view(),
        name='home_view'
    ),
    url(
        r'^(?P<city>[\w-]+)/(?P<time>[\w-]+)/$',
        views.EventByTimeView.as_view(),
        name='event_by_time_view'
    ),
    url(
        r'^(?P<city>[\w-]+)/(?P<time>[\w-]+)/(?P<category>[\w-]+)/$',
        views.EventByCategoryView.as_view(),
        name='event_by_category_view'
    ),
]
