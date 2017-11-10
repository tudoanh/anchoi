from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.jobstores import register_events
import facebook_bot


scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
register_events(scheduler)
scheduler.start()


def crawl_events(lat, lon, distance):
    pass
