from seleccion import seleccionar_libro
from movimientos import registrar_movimiento

def ajuste_de_stock(inventario, registro_movimientos):
    isbn = seleccionar_libro(inventario)

    while True:
        try:
            nueva_cantidad = int(
                input(f"Ingrese la nueva cantidad para '{inventario[isbn]['titulo']}': ")
            )

            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue

            diferencia = nueva_cantidad - inventario[isbn]["cantidad"]
            inventario[isbn]["cantidad"] = nueva_cantidad

            registrar_movimiento(
                registro_movimientos,
                isbn,
                inventario[isbn]["titulo"],
                diferencia,
                "Ajuste"
            )

            print("Stock ajustado correctamente.")
            break

        except ValueError:
            print("Debe ingresar un número entero.")
