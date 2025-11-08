from view.menu_libro import menu_libros
from view.menu_categoria import menu_categorias

def main_menu():
    while True:
        print("\n=== GESTOR DE BIBLIOTECA ===")
        print("1. Gestion de Libros")
        print("2. Gestion de Categorías")
        print("0. Salir")
        op = input("Seleccione una opcion: ")

        if op == "1":
            menu_libros()
        elif op == "2":
            menu_categorias()
        elif op == "0":
            print("saliendo...")
            break
        else:
            print("opcion invalida, intente de nuevo")
