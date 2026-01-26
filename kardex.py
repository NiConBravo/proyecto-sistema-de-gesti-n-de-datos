def mostrar_kardex(registro, tipo=None):
    print("\n📦 KARDEX – HISTORIAL DE MOVIMIENTOS")
    print("-" * 60)

    movimientos = registro
    if tipo:
        movimientos = [m for m in movimientos if m["tipo"] == tipo]

    if not movimientos:
        print("No hay movimientos registrados.")
        return

    for i, m in enumerate(movimientos, start=1):
        print(
            f"{i:02}. {m['titulo']} | ISBN: {m['isbn']} | "
            f"{m['tipo'].upper():7} | "
            f"{m['cantidad_inicial']} → {m['cantidad_final']}"
        )
