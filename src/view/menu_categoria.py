from controller import categoria_controller as ctrl_cat
from utils.validaciones import validar_texto

def menu_categorias():
    while True:
        print("\n---------- MENU DE CATEGORIAS ----------")
        print("1. Crear categoria")
        print("2. Listar categorias")
        print("3. Eliminar categoria")
        print("0. Volver")

        op = input("Seleccione una opcion: ")

        if op == "1":
            nombre = input("Nombre: ")
            descripcion = input("Descripcion: ")
            if not (
                validar_texto(nombre, "Nombre")
                and validar_texto(descripcion, "Descripcion")
            ):
                continue
            ctrl_cat.insertar(nombre, descripcion)
            print("Categoria creada correctamente.")

        elif op == "2":
            categorias = ctrl_cat.listar()
            if not categorias:
                print("No hay categorias registradas.")
                continue
            print("\nID | Nombre | Descripcion")
            print("-" * 40)
            for c in categorias:
                print(f"{c.id_categoria} | {c.nombre} | {c.descripcion}")

        elif op == "3":
            nombre = input("Nombre de la categoria a eliminar: ")
            if not validar_texto(nombre, "Nombre"):
                continue
            eliminadas = ctrl_cat.eliminar_por_nombre(nombre)
            if eliminadas > 0:
                print(f"{eliminadas} categoria(s) eliminada(s).")
            else:
                print("No se encontro una categoria con ese nombre.")

        elif op == "0":
            break
        else:
            print("Opcion invalida.")
