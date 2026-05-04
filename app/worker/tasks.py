from app.extension import celery_app, SessionLocal
from app.models.hobby import Hobby

@celery_app.task
def insert_db(name, hobbies):

    db = SessionLocal()
    try:
        db.add(Hobby(name=name, hobby=hobbies))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        raise 
    finally:
        db.close()