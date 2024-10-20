from toxicbygnn.database.schema import Chemical, Model, Endpoint, Prediction
from toxicbygnn.database import engine

from sqlalchemy import select
from sqlalchemy.orm import Session


def createAllEntitites(entities: list):
    with Session(engine) as session:
        session.add_all(entities)
        session.commit()

def getAllFromTable(table) -> list:
    stmt = select(table)
    with Session(engine) as session:    
        res = session.scalars(stmt)
        return res.all()




endpoints = [
    Endpoint(name="Cancer"),
    Endpoint(name="Sperm")
]




