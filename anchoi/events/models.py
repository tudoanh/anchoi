from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.postgres.fields import JSONField
from django.utils.dateparse import parse_datetime
from django.utils.text import slugify

from unidecode import unidecode


class FacebookPage(models.Model):
    '''
    Facebook Page Model, contain Page ID for later crawl jobs
    '''

    id = models.AutoField(primary_key=True, unique=True)
    page_id = models.CharField(max_length=20, unique=True)

    def __repr__(self):
        return self.page_id


class Event(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
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

    objects = models.GeoManager()
    point = models.PointField(null=True, spatial_index=True, geography=True)

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
        if self.latitude and self.longitude:
            self.point = Point((self.latitude, self.longitude))

        super(Event, self).save(*args, **kwargs)
