"""
Módulo de entrada de stock.

Responsabilidad:
Permitir el ingreso de stock a los libros registrados en el inventario
y registrar el movimiento correspondiente en el Kardex, incluyendo
el estado inicial y final del stock.

Este módulo es invocado desde el menú principal (main.py).
"""

from seleccion import seleccionar_libro
from movimientos import registrar_movimiento


def entrada_stock(inventario_libros, registro_movimientos):
    """
    Realiza una entrada de stock para un libro seleccionado por el usuario.

    Flujo de la operación:
    1. Permite al usuario seleccionar un libro del inventario.
    2. Valida que la selección sea válida.
    3. Solicita una cantidad positiva de stock a ingresar.
    4. Calcula el stock inicial y el stock final.
    5. Actualiza el inventario.
    6. Registra el movimiento de tipo "Ingreso" en el Kardex.

    Parámetros:
    - inventario_libros (dict): Inventario de libros indexado por ISBN.
      Cada libro contiene título, autor y cantidad disponible.
    - registro_movimientos (list): Lista que almacena el historial
      de movimientos del inventario.

    Retorna:
    - None. La función modifica el inventario y el registro por referencia.
    """

    # Selección del libro a modificar
    isbn = seleccionar_libro(inventario_libros)

    # Si no se selecciona un libro (inventario vacío o cancelación), se aborta la operación
    if not isbn:
        return

    # Bucle de validación de la cantidad ingresada
    while True:
        try:
            cantidad = int(input(
                f"Ingrese la cantidad a ingresar para '{inventario_libros[isbn]['titulo']}': "
            ))

            # Validación: la cantidad debe ser un entero positivo
            if cantidad <= 0:
                print("La cantidad debe ser positiva.")
                continue

            # Stock antes del movimiento
            cantidad_inicial = inventario_libros[isbn]["cantidad"]

            # Actualización del inventario
            inventario_libros[isbn]["cantidad"] += cantidad

            # Stock después del movimiento
            cantidad_final = inventario_libros[isbn]["cantidad"]

            # Registro del movimiento en el Kardex
            registrar_movimiento(
                registro_movimientos,
                isbn,
                inventario_libros[isbn]["titulo"],
                cantidad_inicial,
                cantidad_final,
                "Ingreso"
            )

            print("Stock actualizado correctamente.")
            break

        # Manejo de error: entrada no numérica
        except ValueError:
            print("Debe ingresar un número entero.")
