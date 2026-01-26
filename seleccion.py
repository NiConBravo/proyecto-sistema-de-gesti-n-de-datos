def seleccionar_libro(inventario):
    if not inventario:
        print("No hay libros registrados.")
        return None

    libros = list(inventario.items())
    for i, (isbn, info) in enumerate(libros, 1):
        print(f"{i}. {info['titulo']} (ISBN: {isbn})")

    while True:
        try:
            opcion = int(input("Seleccione el número del libro: "))
            if 1 <= opcion <= len(libros):
                return libros[opcion - 1][0]
            print("Número fuera de rango.")
        except ValueError:
            print("Entrada no válida.")
