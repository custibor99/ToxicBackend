from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import declarative_base
from pgvector.sqlalchemy import Vector
from datetime import datetime

FINGERPRINT_SIZE = 2048
DESCRIPTORS_SIZE = 210

Base = declarative_base()


class Chemical(Base):
    __tablename__ = 'chemical'
    id = mapped_column(Integer, primary_key=True)
    smile = mapped_column(String(200), nullable=False, unique=True)
    standardized_smile = mapped_column(String(200), nullable=False, unique=True)

class Descriptors(Base):
    __tablename__ = 'descriptors'
    id = mapped_column(Integer, primary_key=True)
    chemicalId = mapped_column(Integer(), nullable=False, unique=True)
    descriptor = mapped_column(Vector(DESCRIPTORS_SIZE)) #MAKE SPARSE
    raise NotImplementedError("Add relations")

class Fingerprint():
    __tablename__ = 'fingerprints'
    id = mapped_column(Integer, primary_key=True)
    chemicalId = mapped_column(Integer(), nullable=False, unique=True)
    fingerprint = mapped_column(Vector(FINGERPRINT_SIZE))
    raise NotImplementedError("Add relations")

class Model():
    __tablename__ = 'model'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), nullable=False, unique=True)
    type = mapped_column(Enum("classic", "deep", name="type_enum"))


class Endpoint():
    raise NotImplementedError()

class Prediction():
    raise NotImplementedError()
