from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# clase base para modelos ORM
Base = declarative_base()

# directorio para almacenar db
DATA_DIR = Path("datos")
DATA_DIR.mkdir(exist_ok=True)

# url ---> sqlite
DB_URL = f"sqlite:///{(DATA_DIR / 'biblioteca.db').as_posix()}"

# engine
engine = create_engine(DB_URL, echo=True, future=True)

# fabrica de seciones
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)