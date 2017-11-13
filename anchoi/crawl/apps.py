from django.apps import AppConfig

import django_rq


class CrawlConfig(AppConfig):
    name = 'crawl'

    def ready(self):
        from .tasks import (
            daily_scan,
            hourly_scan,
            weekly_page_scan,
            HANOI_CENTER,
            SAIGON_CENTER,
        )

        scheduler = django_rq.get_scheduler('default')

        # Delete any existing jobs in the scheduler when the app starts up
        for job in scheduler.get_jobs():
            job.delete()

        # Scan all page in city in Friday each week
        scheduler.cron(
            "0 0 * * 0",
            func=weekly_page_scan,
            kwargs={
                'lat': HANOI_CENTER[0],
                'lon': HANOI_CENTER[1],
                'distance': 8000,
            }
        )

        scheduler.cron(
            "0 0 * * 1",
            func=weekly_page_scan,
            kwargs={
                'lat': SAIGON_CENTER[0],
                'lon': SAIGON_CENTER[1],
                'distance': 10000,
            }
        )

        # Scan events each day from pages
        scheduler.cron(
            "0 0 * * *",
            func=daily_scan,
        )

        # Update events every hour
        scheduler.cron(
            "0 * * * * ",
            func=hourly_scan
        )
