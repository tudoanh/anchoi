from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^v1.0/events/(?P<pk>[0-9]+)$',
        views.EventDetail.as_view(),
        name='get_delete_put_event'
    ),
    url(
        r'^v1.0/events/$',
        views.EventList.as_view(),
        name='get_post_events'
    )
]
