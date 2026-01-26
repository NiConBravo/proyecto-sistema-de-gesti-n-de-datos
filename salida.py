from seleccion import seleccionar_libro
from movimientos import registrar_movimiento

def salida_stock(inventario, registro_movimientos):
    isbn = seleccionar_libro(inventario)

    while True:
        try:
            cantidad = int(input(
                f"Ingrese la cantidad a retirar de '{inventario[isbn]['titulo']}': "
            ))

            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
                continue

            if cantidad > inventario[isbn]["cantidad"]:
                print("Stock insuficiente.")
                continue

            inventario[isbn]["cantidad"] -= cantidad

            registrar_movimiento(
                registro_movimientos,
                isbn,
                inventario[isbn]["titulo"],
                -cantidad,
                "Salida"
            )

            print("Salida registrada correctamente.")
            break

        except ValueError:
            print("Debe ingresar un número entero.")
