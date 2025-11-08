from controller import libro_controller as ctrl_libros

def menu_libros():
    while True:
        print("\n----------Menu de libros :)---------")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Buscar por categoria")
        print("4. Actualizar precio")
        print("5. Eliminar libro")
        print("0. Volver")

        op = input("Seleccione una opcion :")

        if op == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            precio = float(input("Precio: "))
            categoria_id = int(input("ID de la categoría: "))
            ctrl_libros.insertar(titulo, autor, precio, categoria_id)

        elif op == "2":
            libros = ctrl_libros.listar()
            print("\nID | Título | Autor | Precio | Categoría")
            print("-"*45)
            for l in libros:
                print(f"{l.id} | {l.titulo} | {l.autor} | {l.precio:.2f} | {l.categoria_id}")

        elif op == "3":
            cat = int(input("ID de categoría: "))
            for l in ctrl_libros.buscar_por_categoria(cat):
                print(l)

        elif op == "4":
            t = input("Titulo del libro a actualizar: ")
            nuevo_precio = float(input("Nuevo precio: "))
            if ctrl_libros.actualizar_precio(t, nuevo_precio):
                print("Precio actualizado.")
            else:
                print("Libro no encontrado.")

        elif op == "5":
            t = input("Titulo del libro a eliminar: ")
            n = ctrl_libros.eliminar_por_titulo(t)
            print(f"{n} registros eliminados.")

        elif op == "0":
            break
        else:
            print("opcion invalida")