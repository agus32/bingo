from src.bingo import carton

def test_no_menor():
    mi_carton = carton()
    contador = 0
    celda_vacia = 0
    contador = 0
    for fila in range(0, 3):
        for columna in range(0, 9):
            if mi_carton[fila][columna] != celda_vacia:
                contador = contador+1
    # Esperamos encontrar no menos de 15 celdas ocupadas.
    assert contador >= 15
