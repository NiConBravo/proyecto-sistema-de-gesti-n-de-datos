"""
Módulo de ajuste de stock.

Responsabilidad:
Permitir modificar manualmente la cantidad de stock de un libro
seleccionado por el usuario y registrar el cambio en el Kardex.
Es útil para correcciones, auditorías o actualizaciones por inventario físico.
"""

from seleccion import seleccionar_libro
from movimientos import registrar_movimiento


def ajuste_de_stock(inventario_libros, registro_movimientos):
    """
    Ajusta la cantidad de stock de un libro seleccionado.

    Flujo de la operación:
    1. Permite al usuario seleccionar un libro del inventario.
    2. Solicita la nueva cantidad de stock.
    3. Valida que la cantidad sea un número entero no negativo.
    4. Actualiza el inventario con la nueva cantidad.
    5. Registra el movimiento de tipo "Ajuste" en el Kardex,
       incluyendo la cantidad inicial y final.

    Parámetros:
    - inventario_libros (dict): Diccionario con los libros del inventario,
      indexado por ISBN. Cada libro tiene 'titulo', 'autor' y 'cantidad'.
    - registro_movimientos (list): Lista que almacena el historial de
      movimientos del inventario (Kardex).

    Retorna:
    - None. La función modifica el inventario y el registro por referencia.
    """

    # Selección del libro a ajustar
    isbn = seleccionar_libro(inventario_libros)

    # Si no se selecciona un libro, se aborta la operación
    if not isbn:
        return

    # Bucle de validación de la nueva cantidad ingresada
    while True:
        try:
            nueva_cantidad = int(
                input(f"Ingrese la nueva cantidad para '{inventario_libros[isbn]['titulo']}': ")
            )

            # Validación: la cantidad no puede ser negativa
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue

            # Registrar stock inicial
            cantidad_inicial = inventario_libros[isbn]["cantidad"]

            # Actualizar inventario
            inventario_libros[isbn]["cantidad"] = nueva_cantidad

            # Stock final
            cantidad_final = nueva_cantidad

            # Registrar movimiento en Kardex
            registrar_movimiento(
                registro_movimientos,
                isbn,
                inventario_libros[isbn]["titulo"],
                cantidad_inicial,
                cantidad_final,
                "Ajuste"
            )

            print("Stock ajustado correctamente.")
            break

        # Manejo de error: entrada no numérica
        except ValueError:
            print("Debe ingresar un número entero.")
