"""
Módulo de salida de stock.

Responsabilidad:
Permitir el retiro de stock del inventario de libros y registrar
el movimiento correspondiente en el Kardex, asegurando que no se
retire una cantidad mayor al stock disponible.

Este módulo es invocado desde el menú principal (main.py).
"""

from seleccion import seleccionar_libro
from movimientos import registrar_movimiento


def salida_stock(inventario_libros, registro_movimientos):
    """
    Realiza una salida de stock para un libro seleccionado por el usuario.

    Flujo de la operación:
    1. Permite al usuario seleccionar un libro del inventario.
    2. Valida que la selección sea válida.
    3. Solicita una cantidad positiva a retirar.
    4. Verifica que exista stock suficiente.
    5. Calcula el stock inicial y el stock final.
    6. Actualiza el inventario.
    7. Registra el movimiento de tipo "Salida" en el Kardex.

    Parámetros:
    - inventario_libros (dict): Inventario de libros indexado por ISBN.
      Cada libro contiene título, autor y cantidad disponible.
    - registro_movimientos (list): Lista que almacena el historial
      de movimientos del inventario.

    Retorna:
    - None. La función modifica el inventario y el registro por referencia.
    """

    # Selección del libro del cual se retirará stock
    isbn = seleccionar_libro(inventario_libros)

    # Si no se selecciona un libro (inventario vacío o cancelación), se aborta la operación
    if not isbn:
        return

    # Bucle de validación de la cantidad a retirar
    while True:
        try:
            cantidad = int(input(
                f"Ingrese la cantidad a retirar de '{inventario_libros[isbn]['titulo']}': "
            ))

            # Validación: la cantidad debe ser mayor a cero
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
                continue

            # Validación: no se puede retirar más stock del disponible
            if cantidad > inventario_libros[isbn]["cantidad"]:
                print("Stock insuficiente.")
                continue

            # Stock antes del movimiento
            cantidad_inicial = inventario_libros[isbn]["cantidad"]

            # Actualización del inventario
            inventario_libros[isbn]["cantidad"] -= cantidad

            # Stock después del movimiento
            cantidad_final = inventario_libros[isbn]["cantidad"]

            # Registro del movimiento en el Kardex
            registrar_movimiento(
                registro_movimientos,
                isbn,
                inventario_libros[isbn]["titulo"],
                cantidad_inicial,
                cantidad_final,
                "Salida"
            )

            print("Salida registrada correctamente.")
            break

        # Manejo de error: entrada no numérica
        except ValueError:
            print("Debe ingresar un número entero.")
