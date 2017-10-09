from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1.0/events/(?P<pk>[0-9]+)$',
        views.EventDetail.as_view(),
        name='get_delete_put_event'
    ),
    url(
        r'^api/v1.0/events/$',
        views.get_post_events,
        name='get_post_events'
    )
]
