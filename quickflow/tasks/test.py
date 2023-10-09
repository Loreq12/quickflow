from quickflow.tasks.celery import celery_app


@celery_app.task
def test_task(x, y):
    return x + y
