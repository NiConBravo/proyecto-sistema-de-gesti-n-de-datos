def registrar_movimiento(
    registro_movimientos,
    isbn,
    titulo,
    cantidad_inicial,
    cantidad_final,
    tipo
):
    registro_movimientos.append({
        "isbn": isbn,
        "titulo": titulo,
        "cantidad_inicial": cantidad_inicial,
        "cantidad_final": cantidad_final,
        "tipo": tipo
    })
