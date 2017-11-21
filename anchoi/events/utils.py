from django.utils.dateparse import parse_datetime


categories = {
    'movie': ['phim', 'movie', 'điện ảnh', 'chiếu', 'film', 'actor', 'actress'
              'premiere', 'director', 'đạo diễn', ' cast', 'scriptwriter',
              'cartoon', 'hoạt hình', 'comedy', 'documentary', 'scene'
              'horror', 'sci-fi', 'popcorn'],
    'music': ['music', 'nhạc', 'âm thanh', 'dj', 'ca sĩ', 'nghệ sĩ', 'âm nhạc',
              'nhịp điệu', 'beat', 'harmony', 'rhythm', 'melody', 'hip hop'
              'composer', 'musician', 'edm', 'pop', 'rap', 'rock',
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
                   'chia sẻ', ],
    'education': ['learn', 'study', 'du học', 'học bổng', 'lớp học',
                  'learning', 'dạy', 'lesson', 'research', 'college',
                  'univerity', 'tutorial', 'hướng dẫn', 'education',
                  'class', 'campus', 'school', 'hội thảo', 'seminar']
}


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
