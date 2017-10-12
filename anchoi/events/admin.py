from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'latitude', 'longitude')


admin.site.register(Event, EventAdmin)
