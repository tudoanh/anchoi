import calendar
from datetime import datetime, time, timedelta
from functools import reduce
import operator
import pytz

from django.conf import settings
from django.db.models import Q
from django.utils import timezone

from events.utils import categories


cities = {
    'hanoi': 'Hanoi',
    'saigon': 'Ho Chi Minh City'
}

TIME_ZONE = settings.TIME_ZONE


def generate_date(date_time):
    tz = pytz.timezone(TIME_ZONE)
    return datetime.combine(timezone.now().astimezone(tz).date(), time.min)


def generate_date_range(start, end):
    # See more at https://goo.gl/bSovS9
    # m is time.min/time.max
    tz = pytz.timezone(TIME_ZONE)
    return (
        tz.localize(datetime.combine(start.astimezone(tz).date(), time.min)),
        tz.localize(datetime.combine(end.astimezone(tz).date(), time.max))
    )


def weekday_datetime(n):
    """
    Generate datetime object for given weekday of current week.
    1 is Monday & 7 is Sunday.
    """
    return timezone.now() + timedelta(
        days=(n - timezone.now().isoweekday())
    )


def this_month_datetime():
    today = timezone.now()
    first_day = today + timedelta(
        days=(1 - today.day)
    )
    last_day = today + timedelta(
        days=(
            calendar.monthrange(
                today.year,
                today.month
            )[1] - today.day
        )
    )
    return (today, last_day)


month = this_month_datetime()

date_rage = {
    'today': generate_date_range(timezone.now(), timezone.now()),
    'weekend': generate_date_range(
        weekday_datetime(6),
        weekday_datetime(7)
    ),
    'week': generate_date_range(
        timezone.now(),
        weekday_datetime(7)
    ),
    'month': generate_date_range(*month)
}


def queryset_for(category):
    try:
        query = reduce(
            operator.or_,
            (Q(name__icontains=keyword)
                for keyword in categories.get(category, []))
        )
    except TypeError:
        query = Q(name__icontains='')

    return query
