def registrar_movimiento(registro, isbn, titulo, cantidad, tipo):
    registro.append({
        "isbn": isbn,
        "titulo": titulo,
        "cantidad": cantidad,
        "tipo": tipo
    })
