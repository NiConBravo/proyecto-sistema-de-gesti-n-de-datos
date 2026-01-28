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
from kardex import mostrar_kardex #función para reportar movimientos de inventario
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


# Variable de control para dar inicio al bucle del menú principal
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

    # ===============================================
# Gestión del menú principal del sistema
# ===============================================
# Este bloque controla la navegación del usuario
# dentro del sistema de administración de inventario.
# A partir de la opción ingresada, se delega la
# ejecución al módulo correspondiente.
# ===============================================

# Lectura de la opción seleccionada por el usuario.
# Se convierte a minúscula para evitar errores por
# diferencias de capitalización (ej. "S" vs "s").
opcion = input("Ingrese su opción: ").lower()


# ------------------------------------------------
# Opción 1 – Registro de un nuevo libro
# ------------------------------------------------
# Llama al módulo crear_producto.py.
# Permite agregar un nuevo libro al inventario
# o reemplazar uno existente según su ISBN.
if opcion == "1":
    añadir_libro(inventario_libros)


# ------------------------------------------------
# Opción 2 – Entrada de stock
# ------------------------------------------------
# Llama al módulo entrada.py.
# Incrementa la cantidad disponible de un libro
# seleccionado y registra el movimiento en el Kardex.
elif opcion == "2":
    entrada_stock(inventario_libros, registro_movimientos)


# ------------------------------------------------
# Opción 3 – Salida de stock
# ------------------------------------------------
# Llama al módulo salida.py.
# Reduce la cantidad de stock de un libro,
# validando que exista disponibilidad suficiente,
# y registra la operación en el Kardex.
elif opcion == "3":
    salida_stock(inventario_libros, registro_movimientos)


# ------------------------------------------------
# Opción 4 – Ajuste manual de stock
# ------------------------------------------------
# Llama al módulo ajuste.py.
# Permite corregir directamente la cantidad de
# un libro (por auditoría o inventario físico),
# dejando trazabilidad en el Kardex.
elif opcion == "4":
    ajuste_de_stock(inventario_libros, registro_movimientos)


# ------------------------------------------------
# Opción 5 – Visualización del Kardex
# ------------------------------------------------
# Llama al módulo kardex.py.
# Muestra el historial de movimientos de inventario,
# incluyendo entradas, salidas y ajustes.
elif opcion == "5":
    mostrar_kardex(registro_movimientos)


# ------------------------------------------------
# Opción 6 – Reporte de alertas de stock
# ------------------------------------------------
# Llama al módulo consulta.py.
# Analiza el inventario y detecta productos con
# stock bajo o agotado, mostrando alertas visuales.
elif opcion == "6":
    gestionar_stock(inventario_libros)


    # Opción de salida del sistema pulsando la letra s. Se imprime el mensaje de despedida y se termina el bucle.
    elif opcion == "s":
        print("Gracias por usar el sistema.")

    # Manejo de opción inválida
    else:
        print("Opción inválida.")
