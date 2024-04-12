import time

from celery import shared_task


@shared_task(name="process")
def process():
    time.sleep(10)
    return f"Processing data"
