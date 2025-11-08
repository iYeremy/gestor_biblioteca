from typing import Iterable
from sqlalchemy import select, update, delete, func
from sqlalchemy.exc import SQLAlchemyError
from models.categoria import Categoria
from models.base import session_scope


def insertar(nombre: str, descripcion: str) -> None:
    """Crea una categoría y confirma la transacción."""
    with session_scope() as session:
        nueva_categoria = Categoria(nombre=nombre, descripcion=descripcion)
        session.add(nueva_categoria)


def listar() -> Iterable[Categoria]:
    """Retorna las categorías ordenadas por su ID."""
    with session_scope() as session:
        stmt = select(Categoria).order_by(Categoria.id_categoria.asc())
        return session.scalars(stmt).all()


def buscar_por_nombre(nombre: str) -> Iterable[Categoria]:
    """Filtra categorías por nombre."""
    with session_scope() as session:
        stmt = (
            select(Categoria)
            .where(Categoria.nombre == nombre)
            .order_by(Categoria.nombre.asc())
        )
        return session.scalars(stmt).all()


def actualizar_nombre(nombre_actual: str, nuevo_nombre: str) -> bool:
    """
    Actualiza el nombre de la primera categoría que coincida con el nombre actual.
    Retorna True si se actualizó algún registro.
    """
    try:
        with session_scope() as session:
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
            return True

    except SQLAlchemyError as e:
        print("Error en actualizacion. Transaccion revertida.")
        print("Detalle:", e)
        return False


def eliminar_por_nombre(nombre: str) -> int:
    """Elimina categorías por nombre. Retorna la cantidad eliminada."""
    try:
        with session_scope() as session:
            count_stmt = select(func.count()).where(Categoria.nombre == nombre)
            total = session.execute(count_stmt).scalar_one()

            if total == 0:
                return 0

            stmt = delete(Categoria).where(Categoria.nombre == nombre)
            session.execute(stmt)
            return total

    except SQLAlchemyError as e:
        print("Error en eliminacion. Transaccion revertida.")
        print("Detalle:", e)
        return 0
