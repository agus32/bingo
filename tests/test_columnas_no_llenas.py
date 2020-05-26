from src.bingo import carton

def test_columnas_no_llenas():
    mi_carton = carton()
    celda_vacia = 0
    contador = 0
    for columna in range(0, 9):
        for fila in range(0, 3):
            if mi_carton[fila][columna] != celda_vacia:
                contador = contador + 1
        assert contador < 3
        contador = 0
