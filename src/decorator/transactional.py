from src.core.db import Session

def transactional(func):
    def inner(*args, **kwargs):
        session = Session()
        try:
            result = func(*args, **kwargs)
            session.commit()
            return result
        except:
            session.rollback()
            raise
        finally:
            Session.remove()
    return inner