"""
Módulo de registro de movimientos de inventario (Kardex).

Responsabilidad:
Centralizar el registro de todas las operaciones que modifican el stock
(entradas, salidas y ajustes), almacenando el estado inicial y final
de cada movimiento para permitir auditoría y trazabilidad.
"""


def registrar_movimiento(
    registro_movimientos,
    isbn,
    titulo,
    cantidad_inicial,
    cantidad_final,
    tipo
):
    """
    Registra un movimiento de inventario en el historial (Kardex).

    Cada movimiento almacena el estado del stock antes y después
    de la operación, permitiendo reconstruir el historial completo
    del inventario.

    Parámetros:
    - registro_movimientos (list): Lista donde se almacenan los movimientos.
    - isbn (str): ISBN del libro afectado por el movimiento.
    - titulo (str): Título del libro.
    - cantidad_inicial (int): Stock antes de realizar el movimiento.
    - cantidad_final (int): Stock después de realizar el movimiento.
    - tipo (str): Tipo de movimiento realizado
      ('Ingreso', 'Salida', 'Ajuste').

    Estructura del movimiento registrado:
    {
        'isbn': str,
        'titulo': str,
        'cantidad_inicial': int,
        'cantidad_final': int,
        'tipo': str
    }

    Retorna:
    - None. El movimiento se agrega al registro por referencia.
    """

    registro_movimientos.append({
        "isbn": isbn,
        "titulo": titulo,
        "cantidad_inicial": cantidad_inicial,
        "cantidad_final": cantidad_final,
        "tipo": tipo
    })
