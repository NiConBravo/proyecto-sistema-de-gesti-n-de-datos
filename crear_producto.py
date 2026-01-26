import re

def añadir_libro(inventario_libros):
    while True:
        isbn = input("Ingrese el ISBN (ej. 978-0141036144): ").strip()

        if not re.match(r"^\d{3}-\d{10}$", isbn):
            print("Formato de ISBN inválido.")
            continue

        if isbn in inventario_libros:
            opcion = input("El ISBN existe. ¿Reemplazar? (s/n): ").lower()
            if opcion != "s":
                continue
        break

    titulo = input("Ingrese el título: ").strip()
    autor = input("Ingrese el autor: ").strip()

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                raise ValueError
            break
        except ValueError:
            print("Cantidad inválida.")

    inventario_libros[isbn] = {
        "titulo": titulo,
        "autor": autor,
        "cantidad": cantidad
    }

    print("Libro agregado / actualizado correctamente.")
