def gestionar_stock(inventario_libros):
    print("\n--- Reporte de Alertas ---")
    STOCK_MINIMO = 5

    productos_alerta = {
        isbn: datos
        for isbn, datos in inventario_libros.items()
        if datos["cantidad"] <= STOCK_MINIMO
    }

    if not productos_alerta:
        print("No se detectaron productos con stock insuficiente.")
    else:
        for isbn, datos in productos_alerta.items():
            nivel_critico = datos["cantidad"] == 0
            emoji = "🚨" if nivel_critico else "⚠️"
            estado = "AGOTADO" if nivel_critico else "STOCK BAJO"

            print(f"{emoji} [{estado}] {datos['titulo']} (ISBN: {isbn})")
            print(f"   Actual: {datos['cantidad']} | Mínimo: {STOCK_MINIMO}")
