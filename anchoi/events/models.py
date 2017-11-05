from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.dateparse import parse_datetime
from django.utils.text import slugify

from unidecode import unidecode


class FacebookPage(models.Model):
    name = models.CharField(max_length=255)
    page_id = models.CharField(max_length=20, unique=True)

    def __repr__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    data = JSONField(blank=True)
    fb_id = models.CharField(max_length=20, unique=True)
    start_time = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=128, null=True)
    facebook_page = models.ForeignKey(
        FacebookPage,
        on_delete=models.CASCADE,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.start_time = parse_datetime(self.data.get('start_time'))
            try:
                place = self.data.get('place')
                location = place.get('location')
                self.latitude = float(location.get('latitude'))
                self.longitude = float(location.get('longitude'))
            except AttributeError:
                self.latitude = None
                self.longitude = None

        self.slug = str(self.pk) + '-' + slugify(unidecode(self.name))

        super(Event, self).save(*args, **kwargs)
