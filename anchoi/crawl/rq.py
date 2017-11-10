import django_rq
import tasks


django_rq.enqueue(tasks.daily_scan)
