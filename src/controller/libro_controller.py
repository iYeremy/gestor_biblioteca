from sqlalchemy import select, update, delete
from typing import Iterable, Optional
from sqlalchemy.exc import SQLAlchemyError
from models.libro import Libro
from models.base import SessionLocal

def insertar(titulo: str, autor: str, precio: float) -> None:
    """crea un libro y da check a la transaccion"""
    session = SessionLocal()
    try:
        nuevo = Libro(titulo=titulo, autor=autor, precio=precio)
        session.add(nuevo)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al agregar, se revirtio la transaccion")
        print("DETALLE:", e)
    finally:
        session.close()

def listar() -> Iterable[Libro]:
    """retorna los libros ordenados por id"""
    session = SessionLocal()
    try:
        stmt = select(Libro).order_by(Libro.id.asc())
        return session.scalars(stmt).all()
    finally:
        session.close()

def buscar_por_autor(autor: str) -> Iterable[Libro]:
    """Filtra libros por autor"""
    session = SessionLocal()
    try:
        stmt = select(Libro).where(Libro.autor == autor).order_by(
        Libro.titulo.asc())
        return session.scalars(stmt).all()
    finally:
        session.close()
