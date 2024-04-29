from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings

engine_ord = create_engine(settings.postgres_url_ord, echo=True)

SessionLocalOrd = sessionmaker(autocommit=False, autoflush=False, bind=engine_ord)



def get_db_ord():
    db_ord = SessionLocalOrd()
    try:
        yield db_ord
    finally:
        db_ord.close()


# def get_db_per():
#     db_per = SessionLocalPer()
#     try:
#         yield db_per
#     finally:
#         db_per.close()
