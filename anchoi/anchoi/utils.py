import pytz
import requests

from django.conf import settings
from django.utils import timezone


API_KEY = settings.TELEGRAM_BOT_API_KEY
CHAT_ID = settings.TELEGRAM_CHAT_ID
TIME_ZONE = settings.TIME_ZONE

URL = 'https://api.telegram.org/bot{0}/sendMessage'.format(API_KEY)


def time_now():
    tz = pytz.timezone(TIME_ZONE)
    return timezone.now().astimezone(tz).strftime('%d/%m/%Y - %H:%M:%S')


def send_msg(msg):
    now = time_now()
    requests.post(
        URL,
        data={
            'chat_id': CHAT_ID,
            'text': '_{}_: *{}*'.format(now, msg),
            'parse_mode': 'Markdown',
        }
    )
