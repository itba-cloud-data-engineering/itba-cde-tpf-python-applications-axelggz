import sqlalchemy
from sqlalchemy import Column, Date, Float, Integer, String, create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

engine = create_engine('postgresql://airflow:airflow@postgres/itba')
cur = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()