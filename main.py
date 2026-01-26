from entrada import entrada_stock
from salida import salida_stock
from ajuste import ajuste_de_stock
from kardex import mostrar_kardex
from consulta import gestionar_stock
from crear_producto import añadir_libro

inventario_libros = {
    "978-0141036144": {"titulo": "El Capital", "autor": "Karl Marx", "cantidad": 15},
    "978-0307474728": {"titulo": "Cien años de soledad", "autor": "G.G. Márquez", "cantidad": 10},
    "978-0618260300": {"titulo": "El Hobbit", "autor": "Tolkien", "cantidad": 8},
    "978-0141036145": {"titulo": "Así habló Zaratustra", "autor": "Friedrich Nietzsche", "cantidad": 15},
    "978-0307474729": {"titulo": "Cien años de soledad", "autor": "G.G. Márquez", "cantidad": 10},
    "978-0618260301": {"titulo": "El Pensamiento Crítico", "autor": "Michel Foucault", "cantidad": 8},
}

registro_movimientos = []

opcion = ""
while opcion != "s":
    print("""
--- Menú de Usuario ---
1. Añadir libro
2. Entrada de stock
3. Salida de stock
4. Ajuste de stock
5. Mostrar kardex (registro de movimientos)
6. Reportar Alertas
s. Salir
""")

    opcion = input("Ingrese su opción: ").lower()

    if opcion == "1":
        añadir_libro(inventario_libros)
    elif opcion == "2":
        entrada_stock(inventario_libros, registro_movimientos)
    elif opcion == "3":
        salida_stock(inventario_libros, registro_movimientos)
    elif opcion == "4":
        ajuste_de_stock(inventario_libros, registro_movimientos)
    elif opcion == "5":
        mostrar_kardex(registro_movimientos)
    elif opcion == "6":
        gestionar_stock(inventario_libros)
    elif opcion == "s":
        print("Gracias por usar el sistema.")
    else:
        print("Opción inválida.")
