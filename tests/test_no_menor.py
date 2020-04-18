from src.bingo import carton

def test_no_menor():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    
    # Esperamos encontrar no menos de 15 celdas ocupadas.
    assert contador >= 15
