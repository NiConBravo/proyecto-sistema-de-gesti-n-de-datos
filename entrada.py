from seleccion import seleccionar_libro
from movimientos import registrar_movimiento

def entrada_stock(inventario, registro_movimientos):
    isbn = seleccionar_libro(inventario)

    while True:
        try:
            cantidad = int(input(
                f"Ingrese la cantidad a ingresar para '{inventario[isbn]['titulo']}': "
            ))

            if cantidad <= 0:
                print("La cantidad debe ser positiva.")
                continue

            inventario[isbn]["cantidad"] += cantidad

            registrar_movimiento(
                registro_movimientos,
                isbn,
                inventario[isbn]["titulo"],
                cantidad,
                "Ingreso"
            )

            print("Stock actualizado correctamente.")
            break

        except ValueError:
            print("Debe ingresar un número entero.")
