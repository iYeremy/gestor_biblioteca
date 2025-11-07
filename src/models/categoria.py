from sqlalchemy import Column, Integer, String, Float
from base import Base

class Categoria(Base):
    """tabla 'categoria'
    - id_categoria: PRIMARY KEY
    - nombre : TEXT
    """
    __tablename__ = "categoria"

    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"""<Categoria id_categoria ={self.id_categoria} nombre='{self.nombre}'>"""
    