from src.bingo import carton

def test_izq_der():
    mi_carton = carton()
    celda_vacia = 0
    for fila in range(0, 3):
        for columna in range(1, 9):
            if mi_carton[fila][columna] != celda_vacia:
                assert mi_carton[fila][columna-1] < mi_carton[fila][columna]
