from sqlalchemy import Column, Integer, String, Float
import base.py as Base

class Libro(Base):
    """tabla 'libros'
    - id: PRIMARY KEY AUTOINC
    - titulo : TEXT
    - autor: TEXT
    - precio: FLOAT
    """
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    precio = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return f"""<Libro id ={self.id} titulo='{self.titulo}' 
        autor='{self.autor}' precio={self.precio:.2f} >"""
    