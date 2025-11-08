from controller import libro_controller as ctrl_libros
from utils.validaciones import validar_texto, validar_precio, validar_id

def menu_libros():
    while True:
        print("\n---------- MENU DE LIBROS ----------")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Buscar por categoria")
        print("4. Actualizar precio")
        print("5. Eliminar libro")
        print("0. Volver")

        op = input("Seleccione una opcion: ")

        if op == "1":
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            try:
                precio = float(input("Precio: "))
                categoria_id = int(input("ID de la categoria: "))
            except ValueError:
                print("Error: ingrese valores numericos validos.")
                continue

            if not (
                validar_texto(titulo, "Titulo")
                and validar_texto(autor, "Autor")
                and validar_precio(precio)
                and validar_id(categoria_id)
            ):
                continue

            ctrl_libros.insertar(titulo, autor, precio, categoria_id)
            print("Libro agregado correctamente.")

        elif op == "2":
            libros = ctrl_libros.listar()
            if not libros:
                print("No hay libros registrados.")
                continue
            print("\nID | Titulo | Autor | Precio | Categoria")
            print("-" * 50)
            for l in libros:
                print(f"{l.id_libro} | {l.titulo} | {l.autor} | {l.precio:.2f} | {l.categoria_id}")

        elif op == "3":
            try:
                cat = int(input("ID de categoria: "))
            except ValueError:
                print("Error: ingrese un numero entero para el ID.")
                continue
            libros = ctrl_libros.buscar_por_categoria(cat)
            if not libros:
                print("No hay libros en esa categoria.")
                continue
            for l in libros:
                print(f"{l.id_libro} | {l.titulo} | {l.autor} | {l.precio:.2f}")

        elif op == "4":
            titulo = input("Titulo del libro a actualizar: ")
            try:
                nuevo_precio = float(input("Nuevo precio: "))
            except ValueError:
                print("Error: ingrese un valor numerico para el precio.")
                continue

            if not validar_texto(titulo, "Titulo") or not validar_precio(nuevo_precio):
                continue

            if ctrl_libros.actualizar_precio(titulo, nuevo_precio):
                print("Precio actualizado correctamente.")
            else:
                print("No se encontro un libro con ese titulo.")

        elif op == "5":
            titulo = input("Titulo del libro a eliminar: ")
            if not validar_texto(titulo, "Titulo"):
                continue
            eliminados = ctrl_libros.eliminar_por_titulo(titulo)
            print(f"{eliminados} registro(s) eliminado(s).")

        elif op == "0":
            break
        else:
            print("Opcion invalida.")
