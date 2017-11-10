from django.apps import AppConfig
import django_rq
import tasks


class CrawlConfig(AppConfig):
    name = 'crawl'

    def ready(self):
        scheduler = django_rq.get_scheduler('default')

        # Delete any existing jobs in the scheduler when the app starts up
        for job in scheduler.get_jobs():
            job.delete()

        # Have 'mytask' run every 5 minutes
        scheduler.schedule(datetime.utcnow(), tasks.daily_scan, interval=60)
