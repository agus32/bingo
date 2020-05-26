from src.bingo import carton

def test_nomas_2celdas_llenas_cons():
    mi_carton = carton()
    celda_vacia = 0
    contador = 0
    for fila in range(0, 3):
        for columna in range(0, 9):
            if mi_carton[fila][columna] != celda_vacia:
                contador = contador+1
            else:
                assert contador <= 2
                contador = 0
        contador = 0
