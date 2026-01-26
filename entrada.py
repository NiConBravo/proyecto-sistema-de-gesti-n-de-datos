from seleccion import seleccionar_libro
from movimientos import registrar_movimiento

def entrada_stock(inventario_libros, registro_movimientos):
    isbn = seleccionar_libro(inventario_libros)
    if not isbn:
        return

    while True:
        try:
            cantidad = int(input(
                f"Ingrese la cantidad a ingresar para '{inventario_libros[isbn]['titulo']}': "
            ))

            if cantidad <= 0:
                print("La cantidad debe ser positiva.")
                continue

            cantidad_inicial = inventario_libros[isbn]["cantidad"]
            inventario_libros[isbn]["cantidad"] += cantidad
            cantidad_final = inventario_libros[isbn]["cantidad"]

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

        except ValueError:
            print("Debe ingresar un número entero.")
