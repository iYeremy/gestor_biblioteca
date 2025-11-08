from controller import categoria_controller as ctrl_cat

def menu_categorias():
    while True:
        print("\n--- MENU CATEGORIAS ---")
        print("1. Crear categoría")
        print("2. Listar categorias")
        print("3. Eliminar categoría")
        print("0. Volver")

        op = input("Seleccione una opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            descripcion = input("Descripcion: ")
            ctrl_cat.insertar(nombre, descripcion)

        elif op == "2":
            categorias = ctrl_cat.listar()
            print("\nID | Nombre | Descripcion")
            print("-"*35)
            for c in categorias:
                print(f"{c.id} | {c.nombre} | {c.descripcion}")

        elif op == "3":
            nombre_ = input("Nombre de la categoría a eliminar: ")
            if ctrl_cat.eliminar_por_nombre(nombre_):
                print("Categoría eliminada.")
            else:
                print("No se encontró esa categoría.")

        elif op == "0":
            break
        else:
            print("Opcion invalida.")
