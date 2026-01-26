from seleccion import seleccionar_libro
from movimientos import registrar_movimiento

def salida_stock(inventario_libros, registro_movimientos):
    isbn = seleccionar_libro(inventario_libros)
    if not isbn:
        return

    while True:
        try:
            cantidad = int(input(
                f"Ingrese la cantidad a retirar de '{inventario_libros[isbn]['titulo']}': "
            ))

            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero.")
                continue

            if cantidad > inventario_libros[isbn]["cantidad"]:
                print("Stock insuficiente.")
                continue

            cantidad_inicial = inventario_libros[isbn]["cantidad"]
            inventario_libros[isbn]["cantidad"] -= cantidad
            cantidad_final = inventario_libros[isbn]["cantidad"]

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

        except ValueError:
            print("Debe ingresar un número entero.")
