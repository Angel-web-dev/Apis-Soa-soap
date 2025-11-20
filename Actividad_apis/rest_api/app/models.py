# models.py
from sqlalchemy import Column, Integer, String, Enum
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    telefono = Column(String(20), nullable=True)
    genero = Column(Enum("M", "H", "O"), nullable=False)

class Encuesta(Base):
    __tablename__ = "encuestas"
    id_encuesta = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(String(1000), nullable=True)
    created_by = Column(Integer, nullable=True)  # referencia opcional a usuarios (si quieres, crea FK)
