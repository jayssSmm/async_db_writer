from app.extension import celery_app

@celery_app.task
def insert_db(name, hobbies):
    