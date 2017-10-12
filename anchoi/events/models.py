from django.contrib.postgres.fields import JSONField
from django.utils.dateparse import parse_datetime
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    data = JSONField(blank=True)
    fb_id = models.CharField(max_length=20, unique=True)
    start_time = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            place = self.data.get('place')
            location = place.get('location')
            self.start_time = parse_datetime(self.data.get('start_time'))
            self.latitude = (
                float(location.get('latitude')) if place else None
            )
            self.longitude = (
                float(location.get('longitude')) if place else None
            )
        super(Event, self).save(*args, **kwargs)
