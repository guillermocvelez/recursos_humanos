import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:MySecretPassword*@localhost:5434/DATOS')

Session = sessionmaker(bind=engine)

Base = declarative_base()

