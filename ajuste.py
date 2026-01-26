from seleccion import seleccionar_libro
from movimientos import registrar_movimiento

def ajuste_de_stock(inventario_libros, registro_movimientos):
    isbn = seleccionar_libro(inventario_libros)
    if not isbn:
        return

    while True:
        try:
            nueva_cantidad = int(
                input(f"Ingrese la nueva cantidad para '{inventario_libros[isbn]['titulo']}': ")
            )

            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue

            cantidad_inicial = inventario_libros[isbn]["cantidad"]
            inventario_libros[isbn]["cantidad"] = nueva_cantidad
            cantidad_final = nueva_cantidad

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

        except ValueError:
            print("Debe ingresar un número entero.")
