from pathlib import Path
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from threading import Lock
# clase base para modelos ORM
Base = declarative_base()

# directorio para almacenar db
DATA_DIR = Path("datos")
DATA_DIR.mkdir(exist_ok=True)

# url ---> sqlite
DB_URL = f"sqlite:///{(DATA_DIR / 'biblioteca.db').as_posix()}"

# engine
engine = create_engine(DB_URL, 
                       echo=True, 
                       future=True,
                       connect_args={"check_same_thread": False} # concurrencia
                       )

# bloqueo global para operaciones concurrentes
lock = Lock()

# fabrica de seciones
SessionFactory = sessionmaker(
    bind=engine, autoflush=False, 
    autocommit=False, future=True, 
    )

# cada hilo obtiene su propia sesion pero aislada
SessionLocal = scoped_session(SessionFactory)

@contextmanager
def session_scope():
    """
    CM seguro para manejar sesiones:
    -crea una sesion temporal
    -hace commit si todo va bien
    -hace rollback si hay error
    -cierra sesion despues"""
    session = SessionLocal()
    try:
        with lock: # exclusion mutua
            yield session
            session.commit()
    except Exception as e:
        session.rollback()
        print("Error en la transaccion", e)
        raise
    finally:
        session.close()

def init_db() -> None:
    """Crea las tablas si no existen aun."""
    from . import categoria, libro  # pylint: disable=unused-import

    Base.metadata.create_all(bind=engine)
