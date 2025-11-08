def validar_texto(valor: str, campo: str, min_len: int = 1, max_len: int = 100) -> bool:
    if not valor or not valor.strip():
        print(f"El campo '{campo}' no puede estar vacío.")
        return False
    if not (min_len <= len(valor) <= max_len):
        print(f"El campo '{campo}' debe tener entre {min_len} y {max_len} caracteres.")
        return False
    return True


def validar_precio(precio: float) -> bool:
    if precio <= 0:
        print("El precio debe ser mayor que cero.")
        return False
    return True


def validar_id(categoria_id: int) -> bool:
    if not isinstance(categoria_id, int) or categoria_id <= 0:
        print("El ID de categoría debe ser un número positivo.")
        return False
    return True