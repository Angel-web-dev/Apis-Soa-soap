# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Usuarios
@router.post("/usuarios", response_model=schemas.UsuarioRead)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_usuario(db, usuario)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/usuarios")
def listar_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_usuarios(db, skip, limit)

@router.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioRead)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    u = crud.get_usuario(db, usuario_id)
    if not u:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return u

@router.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, datos: dict, db: Session = Depends(get_db)):
    return crud.update_usuario(db, usuario_id, datos)

@router.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    crud.delete_usuario(db, usuario_id)
    return {"mensaje": "Usuario eliminado"}

# Encuestas
@router.post("/encuestas", response_model=schemas.EncuestaRead)
def create_encuesta(encuesta: schemas.EncuestaCreate, db: Session = Depends(get_db)):
    return crud.create_encuesta(db, encuesta)

@router.get("/encuestas")
def listar_encuestas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_encuestas(db, skip, limit)

@router.get("/encuestas/{encuesta_id}", response_model=schemas.EncuestaRead)
def obtener_encuesta(encuesta_id: int, db: Session = Depends(get_db)):
    e = crud.get_encuesta(db, encuesta_id)
    if not e:
        raise HTTPException(status_code=404, detail="Encuesta no encontrada")
    return e

@router.put("/encuestas/{encuesta_id}")
def actualizar_encuesta(encuesta_id: int, datos: dict, db: Session = Depends(get_db)):
    return crud.update_encuesta(db, encuesta_id, datos)

@router.delete("/encuestas/{encuesta_id}")
def eliminar_encuesta(encuesta_id: int, db: Session = Depends(get_db)):
    crud.delete_encuesta(db, encuesta_id)
    return {"mensaje": "Encuesta eliminada"}
