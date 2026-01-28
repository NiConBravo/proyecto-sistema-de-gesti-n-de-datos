import re

def añadir_libro(inventario_libros):
    """
    Agrega un nuevo libro al inventario o reemplaza uno existente.

    Solicita al usuario los datos del libro (ISBN, título, autor y cantidad),
    valida el formato del ISBN y controla que la cantidad ingresada sea válida.
    Si el ISBN ya existe, permite al usuario decidir si desea reemplazarlo.

    Args:
        inventario_libros (dict): Diccionario que almacena los libros del inventario.
                                  La clave es el ISBN y el valor es otro diccionario
                                  con 'titulo', 'autor' y 'cantidad'.

    Returns:
        None: La función modifica el inventario directamente e imprime mensajes
              informativos en pantalla.
    """

    # Se inicia el bucle para solicitar el ISBN
    while True:
        isbn = input("Ingrese el ISBN (ej. 978-0141036144): ").strip()

        # Validar formato ISBN (Tres dígitos, un guion, y diez dígitos más)
        if not re.match(r"^\d{3}-\d{10}$", isbn):
            print("Formato de ISBN inválido.")
            continue

        # Verificar si el ISBN ya existe en el inventario y si existe da la opción de reemplazarlo
        if isbn in inventario_libros:
            opcion = input("El ISBN existe. ¿Reemplazar? (s/n): ").lower()
            if opcion != "s":
                continue
        break

    # Se recogen los datos del libro con la función strip para eliminar espacios en blanco en el principio y final
    titulo = input("Ingrese el título: ").strip()
    autor = input("Ingrese el autor: ").strip()

    # Input para que el usuario ingrese la cantidad de libros con una función try para controlar que sea un número entero
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                raise ValueError
            break
        except ValueError:
            print("Cantidad inválida.")

    # Registro del libro en el inventario
    inventario_libros[isbn] = {
        "titulo": titulo,
        "autor": autor,
        "cantidad": cantidad
    }

    # Confirmación de la operación
    print("Libro agregado / actualizado correctamente.")
