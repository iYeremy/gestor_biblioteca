import sys
from pathlib import Path

# agregar src/ a sys.path asi los imports trabajan sin importar donde main.py este
ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from models.base import init_db
from view.menu_principal import main_menu

if __name__ == "__main__":
    init_db()
    main_menu()
