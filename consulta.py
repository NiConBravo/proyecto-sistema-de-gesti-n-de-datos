def gestionar_stock(inventario_libros):
    """
    Analiza el inventario y muestra alertas de stock bajo o agotado.

    Recorre todos los libros del inventario y detecta aquellos cuya
    cantidad es menor o igual al stock mínimo definido. Muestra un
    reporte en consola indicando si el producto tiene stock bajo
    o está completamente agotado.

    Args:
        inventario_libros (dict): Diccionario del inventario de libros.
                                  La clave es el ISBN y el valor es un
                                  diccionario con 'titulo', 'autor' y 'cantidad'.

    Returns:
        None: La función solo muestra información en pantalla y no
              modifica el inventario.
    """

    print("\n--- Reporte de Alertas ---")

    # Nivel mínimo de stock permitido
    STOCK_MINIMO = 5

    # Filtrar libros cuyo stock es menor o igual al mínimo permitido
    productos_alerta = {
        isbn: datos
        for isbn, datos in inventario_libros.items()
        if datos["cantidad"] <= STOCK_MINIMO
    }

    # Verificar si existen productos en estado de alerta
    if not productos_alerta:
        print("No se detectaron productos con stock insuficiente.")
    else:
        for isbn, datos in productos_alerta.items():
            # Determinar si el producto está agotado o con stock bajo
            nivel_critico = datos["cantidad"] == 0
            emoji = "🚨" if nivel_critico else "⚠️"
            estado = "AGOTADO" if nivel_critico else "STOCK BAJO"

            # Mostrar alerta detallada del producto
            print(f"{emoji} [{estado}] {datos['titulo']} (ISBN: {isbn})")
            print(f"   Actual: {datos['cantidad']} | Mínimo: {STOCK_MINIMO}")
