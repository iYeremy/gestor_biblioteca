from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
class Libro(Base):

    """tabla 'libros'
    - id_libro: PRIMARY KEY AUTOINC
    - categoria_id: FOREIGN KEY de categorias(id_categoria)
    - categoria : Relacion muchos(libros) a uno (categorias)
    - titulo : TEXT
    - autor: TEXT
    - precio: FLOAT
    """
    __tablename__ = "libros"

    id_libro = Column(Integer, primary_key=True, autoincrement=True)
    
    # FK hacia categorias
    categoria_id = Column(Integer, ForeignKey("categorias.id_categoria"), nullable=False)
    
    # relacion inversa
    categoria = relationship("Categoria", back_populates="libros")

    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    precio = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return (
            f"<Libro id_libro={self.id_libro} "
            f"categoria_id={self.categoria_id} "
            f"titulo='{self.titulo}' "
            f"autor='{self.autor}' "
            f"precio={self.precio:.2f}>"
        )
