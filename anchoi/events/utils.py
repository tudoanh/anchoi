from datetime import datetime
import pytz


def extract_datetime(date_str):
    timezone = 'Asia/Saigon'
    return pytz.timezone(timezone).localize(
        datetime.strptime(date_str, "%Y-%m-%d")
    )
