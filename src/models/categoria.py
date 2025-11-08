from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Categoria(Base):
    """tabla 'categorias'
    - id_categoria: PRIMARY KEY
    - nombre : TEXT
    - descripcion : TEXT
    - libros: relacion uno(categoria) a muchos (libros)
    """
    __tablename__ = "categorias"

    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)

    # relacion uno a muchos
    libros = relationship("Libro", back_populates="categoria", cascade="all, delete")

    def __repr__(self) -> str:
        return f"""<Categoria id_categoria ={self.id_categoria} nombre='{self.nombre}' descripcion='{self.descripcion}'>"""
    