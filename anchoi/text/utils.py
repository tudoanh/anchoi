import calendar
from datetime import datetime, time, timedelta
from functools import reduce
import operator
import pytz

from django.db.models import Q

from events.utils import categories


cities = {
    'hanoi': 'Hanoi',
    'saigon': 'Ho Chi Minh City'
}


def generate_date(date_time):
    timezone = 'Asia/Ho_Chi_Minh'
    return pytz.timezone(timezone).localize(
        datetime.combine(date_time, time.min)
    )


def generate_date_range(start, end):
    # See more at https://goo.gl/bSovS9
    # m is time.min/time.max
    timezone = 'Asia/Ho_Chi_Minh'
    return (
        pytz.timezone(timezone).localize(
            datetime.combine(start, time.min)
        ),
        pytz.timezone(timezone).localize(
            datetime.combine(end, time.max)
        )
    )


def weekday_datetime(n):
    """
    Generate datetime object for given weekday of current week.
    1 is Monday & 7 is Sunday.
    """
    return datetime.now() + timedelta(
        days=(n - datetime.now().isoweekday())
    )


def this_month_datetime():
    today = datetime.today()
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
    return (first_day, last_day)


month = this_month_datetime()

date_rage = {
    'today': generate_date_range(datetime.now(), datetime.now()),
    'weekend': generate_date_range(
        weekday_datetime(6),
        weekday_datetime(7)
    ),
    'week': generate_date_range(
        weekday_datetime(1),
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
