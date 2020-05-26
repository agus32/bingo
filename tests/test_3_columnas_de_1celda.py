from src.bingo import carton

def test_3_columnas_1celda():
    mi_carton = carton()
    celda_vacia = 0
    contador = 0
    columna_de_1 = 0
    for columna in range(0, 9):
        for fila in range(0, 3):
            if mi_carton[fila][columna] != celda_vacia:
                contador = contador + 1
        if contador == 1:
            columna_de_1 = 1 + columna_de_1
        contador = 0
    assert columna_de_1 == 3
