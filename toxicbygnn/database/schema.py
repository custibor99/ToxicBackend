from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey 
from sqlalchemy.orm import declarative_base, mapped_column
from sqlalchemy.ext.declarative import declarative_base

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
    chemicalId = mapped_column(ForeignKey("chemical.id"), nullable=False, unique=True)
    descriptor = mapped_column(Vector(DESCRIPTORS_SIZE)) #MAKE SPARSE

class Fingerprint(Base):
    __tablename__ = 'fingerprints'
    id = mapped_column(Integer, primary_key=True)
    chemicalId = mapped_column(ForeignKey("chemical.id"), nullable=False, unique=True)
    fingerprint = mapped_column(Vector(FINGERPRINT_SIZE))

class Endpoint(Base):
    __tablename__ = 'endpoint'
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(255), nullable=False, unique=True)

class Model(Base):
    __tablename__ = 'model'
    id = mapped_column(Integer, primary_key=True)
    endpointId = mapped_column(ForeignKey("endpoint.id"), nullable=False)
    name = mapped_column(String(255), nullable=False)
    type = mapped_column(Enum("classic", "deep", name="type_enum"))

class Prediction(Base):
    __tablename__ = "prediction"
    id = mapped_column(Integer, primary_key=True)
    modelId = mapped_column(ForeignKey("model.id"), nullable=False)
    chemicalId = mapped_column(ForeignKey("chemical.id"), nullable=False)
    createdAt = mapped_column(DateTime(), nullable=False)

metadata = Base.metadata