from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy

# Заменяем использование библиотеки sqlite на psycopg2 для PostgreSQL
engine = create_engine('postgresql://postgres:1234@localhost/cookingtg')

Session = sessionmaker(bind=engine)

Base = sqlalchemy.orm.declarative_base()
