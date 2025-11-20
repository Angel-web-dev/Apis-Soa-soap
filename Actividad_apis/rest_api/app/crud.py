# crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import IntegrityError

# Usuarios
def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        email=usuario.email,
        telefono=usuario.telefono,
        genero=usuario.genero
    )
    db.add(db_usuario)
    try:
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except IntegrityError:
        db.rollback()
        raise

def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def update_usuario(db: Session, usuario_id: int, datos: dict):
    db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).update(datos)
    db.commit()
    return get_usuario(db, usuario_id)

def delete_usuario(db: Session, usuario_id: int):
    db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).delete()
    db.commit()

# Encuestas
def create_encuesta(db: Session, encuesta: schemas.EncuestaCreate):
    db_encuesta = models.Encuesta(
        titulo=encuesta.titulo,
        descripcion=encuesta.descripcion,
        created_by=encuesta.created_by
    )
    db.add(db_encuesta)
    db.commit()
    db.refresh(db_encuesta)
    return db_encuesta

def get_encuesta(db: Session, encuesta_id: int):
    return db.query(models.Encuesta).filter(models.Encuesta.id_encuesta == encuesta_id).first()

def get_encuestas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Encuesta).offset(skip).limit(limit).all()

def update_encuesta(db: Session, encuesta_id: int, datos: dict):
    db.query(models.Encuesta).filter(models.Encuesta.id_encuesta == encuesta_id).update(datos)
    db.commit()
    return get_encuesta(db, encuesta_id)

def delete_encuesta(db: Session, encuesta_id: int):
    db.query(models.Encuesta).filter(models.Encuesta.id_encuesta == encuesta_id).delete()
    db.commit()
