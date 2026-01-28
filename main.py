"""
Archivo principal del sistema de administración de productos (libros).

Responsabilidad:
Actuar como punto de entrada del sistema y coordinar la interacción
entre el usuario y los distintos módulos de gestión del inventario.

Funcionalidades accesibles desde el menú:
- Añadir nuevos libros al inventario.
- Realizar entradas, salidas y ajustes de stock.
- Consultar el historial de movimientos (Kardex).
- Gestionar y reportar alertas de stock.

Este archivo no contiene lógica de negocio compleja, sino que
orquesta el flujo del sistema llamando a los módulos correspondientes.
"""

# Importación de módulos funcionales
from entrada import entrada_stock
from salida import salida_stock
from ajuste import ajuste_de_stock
from kardex import mostrar_kardex
from consulta import gestionar_stock
from crear_producto import añadir_libro


# Inventario inicial del sistema
# Estructura:
# {
#   ISBN: {
#       'titulo': str,
#       'autor': str,
#       'cantidad': int
#   }
# }
inventario_libros = {
    "978-0141036144": {"titulo": "El Capital", "autor": "Karl Marx", "cantidad": 15},
    "978-0307474728": {"titulo": "Cien años de soledad", "autor": "G.G. Márquez", "cantidad": 10},
    "978-0618260300": {"titulo": "El Hobbit", "autor": "Tolkien", "cantidad": 8},
    "978-0141036145": {"titulo": "Así habló Zaratustra", "autor": "Friedrich Nietzsche", "cantidad": 15},
    "978-0307474729": {"titulo": "Cien años de soledad", "autor": "G.G. Márquez", "cantidad": 10},
    "978-0618260301": {"titulo": "El Pensamiento Crítico", "autor": "Michel Foucault", "cantidad": 8},
}

# Historial de movimientos del inventario (Kardex)
# Cada movimiento registra:
# - ISBN
# - título
# - cantidad inicial
# - cantidad final
# - tipo de movimiento
registro_movimientos = []


# Variable de control del menú principal
opcion = ""

# Bucle principal del sistema
while opcion != "s":

    # Menú de opciones disponible para el usuario
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

    # Lectura de la opción del usuario
    opcion = input("Ingrese su opción: ").lower()

    # Opción 1: Añadir un nuevo libro al inventario
    if opcion == "1":
        añadir_libro(inventario_libros)

    # Opción 2: Registrar entrada de stock
    elif opcion == "2":
        entrada_stock(inventario_libros, registro_movimientos)

    # Opción 3: Registrar salida de stock
    elif opcion == "3":
        salida_stock(inventario_libros, registro_movimientos)

    # Opción 4: Ajustar stock de un libro
    elif opcion == "4":
        ajuste_de_stock(inventario_libros, registro_movimientos)

    # Opción 5: Mostrar historial de movimientos (Kardex)
    elif opcion == "5":
        mostrar_kardex(registro_movimientos)

    # Opción 6: Gestionar y reportar alertas de stock
    elif opcion == "6":
        gestionar_stock(inventario_libros)

    # Opción de salida del sistema
    elif opcion == "s":
        print("Gracias por usar el sistema.")

    # Manejo de opción inválida
    else:
        print("Opción inválida.")
