"""
Módulo de selección de libros.

Responsabilidad:
Permitir al usuario seleccionar un libro del inventario de forma
interactiva y controlada, devolviendo su ISBN para que otros módulos
puedan operar sobre él (entrada, salida, ajuste de stock, etc.).

Este módulo evita duplicar lógica de selección en distintos puntos
del sistema y mantiene una experiencia de usuario consistente.
"""


def seleccionar_libro(inventario):
    """
    Muestra el inventario disponible y permite seleccionar un libro por número.

    Flujo de la función:
    1. Verifica si el inventario está vacío.
    2. Muestra una lista numerada con los títulos disponibles.
    3. Solicita al usuario un número de selección.
    4. Valida la entrada y devuelve el ISBN correspondiente.

    Parámetros:
    - inventario (dict): Diccionario de libros indexados por ISBN.
      Cada valor contiene información del libro (título, autor, cantidad).

    Retorna:
    - str: ISBN del libro seleccionado.
    - None: Si no hay libros registrados en el inventario.

    Uso típico:
    isbn = seleccionar_libro(inventario_libros)
    if not isbn:
        return
    """

    # Validación inicial: inventario vacío
    if not inventario:
        print("No hay libros registrados.")
        return None

    # Conversión del inventario a lista para permitir selección por índice
    libros = list(inventario.items())

    # Mostrar los libros disponibles de forma numerada
    for i, (isbn, info) in enumerate(libros, 1):
        print(f"{i}. {info['titulo']} (ISBN: {isbn})")

    # Bucle de validación de la selección del usuario
    while True:
        try:
            opcion = int(input("Seleccione el número del libro: "))

            # Validación del rango seleccionado
            if 1 <= opcion <= len(libros):
                # Retorna únicamente el ISBN del libro seleccionado
                return libros[opcion - 1][0]

            print("Número fuera de rango.")

        except ValueError:
            # Manejo de entradas no numéricas
            print("Entrada no válida.")
