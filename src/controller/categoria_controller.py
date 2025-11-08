from typing import Iterable, Optional
from sqlalchemy import select, update, delete, func
from sqlalchemy.exc import SQLAlchemyError
from models.categoria import Categoria
from models.base import SessionLocal


def insertar(nombre: str, descripcion: str) -> None:
    """Crea una categoría y confirma la transacción."""
    session = SessionLocal()
    try:
        nueva_categoria = Categoria(nombre=nombre, descripcion=descripcion)
        session.add(nueva_categoria)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al agregar la categoría, se revirtió la transaccion.")
        print("DETALLE:", e)
    finally:
        session.close()


def listar() -> Iterable[Categoria]:
    """Retorna las categorías ordenadas por su id."""
    session = SessionLocal()
    try:
        stmt = select(Categoria).order_by(Categoria.id_categoria.asc())
        return session.scalars(stmt).all()
    finally:
        session.close()


def buscar_por_nombre(nombre: str) -> Iterable[Categoria]:
    """Filtra categorías por nombre."""
    session = SessionLocal()
    try:
        stmt = (
            select(Categoria)
            .where(Categoria.nombre == nombre)
            .order_by(Categoria.nombre.asc())
        )
        return session.scalars(stmt).all()
    finally:
        session.close()


def actualizar_nombre(nombre_actual: str, nuevo_nombre: str) -> bool:
    """
    Actualiza el nombre de la primera categoría que coincida con el nombre actual.

    Retorna True si se actualizó algun registro.
    """
    session = SessionLocal()
    try:
        existe_stmt = (
            select(Categoria.id_categoria)
            .where(Categoria.nombre == nombre_actual)
            .limit(1)
        )
        if not session.execute(existe_stmt).first():
            return False

        stmt = (
            update(Categoria)
            .where(Categoria.nombre == nombre_actual)
            .values(nombre=nuevo_nombre)
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


def eliminar_por_nombre(nombre: str) -> int:
    """Elimina categorías por nombre. Retorna la cantidad eliminada."""
    session = SessionLocal()
    try:
        count_stmt = select(func.count()).where(Categoria.nombre == nombre)
        total = session.execute(count_stmt).scalar_one()
        if total == 0:
            return 0

        stmt = delete(Categoria).where(Categoria.nombre == nombre)
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
