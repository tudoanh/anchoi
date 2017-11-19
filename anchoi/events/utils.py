import pytz
import requests

from django.conf import settings
from django.utils import timezone
from django.utils.dateparse import parse_datetime


categories = {
    'movie': ['phim', 'movie', 'điện ảnh', 'chiếu', 'film', 'cinema',
              'premiere', 'director', 'đạo diễn', ' cast', 'scriptwriter',
              'kịch ', 'cartoon', 'hoạt hình', 'comedy', 'documentary',
              'horror', 'sci-fi', 'popcorn'],
    'music': ['music', 'nhạc', 'âm thanh', 'dj', 'ca sĩ', 'nghệ sĩ', 'âm nhạc',
              'nhịp điệu', 'beat', 'harmony', 'rhythm', 'melody', 'hip hop'
              'composer', 'musician', 'amp', 'edm', 'pop', 'rap', 'rock',
              'sound', 'concert', 'hymn', 'symphony', 'giao hưởng', 'voice',
              ' hát', 'violin', 'guitar', 'singer', 'bolero', 'band'],
    'sport': ['bóng đá', 'ngoại hạng anh', 'chạy bộ', 'bóng rổ', 'leo núi',
              'đạp xe', 'chèo thuyền', 'lặn', 'yoga', 'cầu lông', 'bida',
              'billards', 'bóng chày', 'bóng chuyền', 'cờ vua', 'cờ tướng',
              'cờ vây', 'poker', 'điền kinh', 'run ', 'hiking', 'diving ',
              'soccer', 'football', 'basketball', 'liên minh', 'board game',
              'ma sói', 'thi đấu'],
    'experience': ['du lịch', 'phượt', 'trải nghiệm', 'travel', ' nomad',
                   'leo núi', 'bụi', 'học làm', 'make', 'craft', 'lớp học',
                   'workshop', 'party', 'tourist', 'kỹ năng', 'skill',
                   'chia sẻ', 'hội thảo', 'seminar'],
    'education': ['learn', 'study', 'du học', 'học bổng', 'lớp học',
                  'learning', 'dạy', 'lesson', 'research', 'college',
                  'univerity', 'tutorial', 'hướng dẫn', 'education',
                  'class', 'campus', 'school']
}

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


def extract_event_data(fb_event):
    try:
        place = fb_event.get('place')
        location = place.get('location')
        event = {
            'name': fb_event['name'],
            'data': fb_event,
            'fb_id': fb_event['id'],
            'start_time': parse_datetime(
                fb_event.get('start_time')
            ),
            'latitude': location.get('latitude'),
            'longitude': location.get('longitude'),
        }
        return event
    except AttributeError:
        event = {
            'name': fb_event['name'],
            'data': fb_event,
            'fb_id': fb_event['id'],
            'start_time': parse_datetime(
                fb_event.get('start_time')
            ),
            'latitude': None,
            'longitude': None,
        }
        return event
