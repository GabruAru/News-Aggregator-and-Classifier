from celery import Celery

app = Celery(
    'celery_web',
    broker='redis://127.0.0.1:6379/0',
    backend='redis://127.0.0.1:6379/0',
    include=['app.classifier']
)