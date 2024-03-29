from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ
from dotenv import load_dotenv


engine = create_engine("")

sessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


#dependency 
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()