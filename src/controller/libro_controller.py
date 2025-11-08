from sqlalchemy import select, update, delete, func
from typing import Iterable, Optional
from sqlalchemy.exc import SQLAlchemyError
from models.libro import Libro
from models.base import SessionLocal

def insertar(titulo: str, autor: str, precio: float, categoria_id: int) -> None:
    """crea un libro y da check a la transaccion"""
    session = SessionLocal()
    try:
        nuevo = Libro(titulo=titulo, autor=autor, precio=precio, categoria_id=categoria_id)
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

def actualizar_precio(titulo: str, nuevo_precio: float) -> bool:
    """
    Actualiza el precio del primer libro con ese título.

    Retorna True si se actualizó algún registro.
    """
    session = SessionLocal()
    try:
        existe_stmt = select(Libro.id_libro).where(Libro.titulo == titulo).limit(1)
        if not session.execute(existe_stmt).first():
            return False
        stmt = (
            update(Libro)
            .where(Libro.titulo == titulo)
            .values(precio=nuevo_precio)
        )
        session.execute(stmt)
        session.commit()
        return True
    except SQLAlchemyError as e:
        session.rollback()
        print("Error en actualización. Transacción revertida.")
        print("Detalle:", e)
        return False
    finally:
        session.close()


def eliminar_por_titulo(titulo: str) -> int:
    """Elimina libros por título. Retorna la cantidad eliminada."""
    session = SessionLocal()
    try:
        count_stmt = select(func.count()).where(Libro.titulo == titulo)
        total = session.execute(count_stmt).scalar_one()
        if total == 0:
            return 0
        stmt = delete(Libro).where(Libro.titulo == titulo)
        session.execute(stmt)
        session.commit()
        return total
    except SQLAlchemyError as e:
        session.rollback()
        print("Error en eliminación. Transacción revertida.")
        print("Detalle:", e)
        return 0
    finally:
        session.close()

def buscar_por_categoria(categoria_id: int):
    """Devuelve los libros que pertenecen a una categoría específica."""
    session = SessionLocal()
    try:
        stmt = (
            select(Libro)
            .where(Libro.categoria_id == categoria_id)
            .order_by(Libro.titulo.asc())
        )
        return session.scalars(stmt).all()
    finally:
        session.close()
