def mostrar_kardex(registro, tipo=None):
    """
    Muestra el historial de movimientos de stock (KARDEX).

    Permite visualizar todos los movimientos registrados o filtrar
    por un tipo específico de movimiento (entrada, salida, ajuste).

    Args:
        registro (list): Lista de diccionarios que representan los movimientos
                         de stock registrados.
        tipo (str, optional): Tipo de movimiento a filtrar.
                              Puede ser 'entrada', 'salida' o 'ajuste'.
                              Si es None, se muestran todos los movimientos.

    Returns:
        None: La función solo imprime información en pantalla.
    """

    # Encabezado del kardex
    print("\n📦 KARDEX – HISTORIAL DE MOVIMIENTOS")
    print("-" * 60)

    # Lista base de movimientos
    movimientos = registro

    # Filtrar movimientos si se especifica un tipo
    if tipo:
        movimientos = [m for m in movimientos if m["tipo"] == tipo]

    # Validar si existen movimientos para mostrar
    if not movimientos:
        print("No hay movimientos registrados.")
        return

    # Encabezado de la tabla
    print(f"{'ID Mov':<3} {'TÍTULO':<20} | {'ISBN':<15} | {'TIPO':<8} | {'MOVIMIENTO'}")
    print("-" * 70)

    # Recorrer y mostrar cada movimiento
    for i, m in enumerate(movimientos, start=1):
        print(
            f"{i:02}. {m['titulo']} | ISBN: {m['isbn']} | "
            f"{m['tipo'].upper():7} | "
            f"{m['cantidad_inicial']} → {m['cantidad_final']}"
        )
