from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from sqlalchemy.engine import URL
from pgvector.psycopg2 import register_vector
import os

from toxicbygnn.database.schema import metadata, Endpoint

print("PREPARING DATABASE CONNECTION")

POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_INIT = bool(os.environ.get('POSTGRES_INIT','0'))

url = URL.create(
    drivername="postgresql",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host="localhost",
    port=POSTGRES_PORT,
    database=POSTGRES_DB
)

engine = create_engine(url)

if POSTGRES_INIT: 
    with engine.connect() as conn:
        conn.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
        conn.commit()
        register_vector(conn)
        metadata.drop_all(bind=conn)
        metadata.create_all(bind=conn, checkfirst=True)

        with open("resources/migration.sql", "r") as file:
            for line in file:
                conn.execute(text(line))
                conn.commit()
    
    