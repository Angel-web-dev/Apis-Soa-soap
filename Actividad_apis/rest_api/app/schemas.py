# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioCreate(BaseModel):
    nombre: str
    apellidos: str
    email: EmailStr
    telefono: Optional[str] = None
    genero: str

class UsuarioRead(UsuarioCreate):
    id_usuario: int

    class Config:
        orm_mode = True

class EncuestaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    created_by: Optional[int] = None

class EncuestaRead(EncuestaCreate):
    id_encuesta: int

    class Config:
        orm_mode = True
