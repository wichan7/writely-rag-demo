from src.core.db import Session

def transactional(func):
    def inner(*args, **kwargs):
        session = Session()
        try:
            func(*args, **kwargs)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            Session.remove()
    return inner