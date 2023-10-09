from celery import Celery

from quickflow.config import get_settings


def create_celery_app() -> Celery:
    settings = get_settings()
    app = Celery('dags', broker=settings.cache.unicode_string())

    return app


celery_app = create_celery_app()
