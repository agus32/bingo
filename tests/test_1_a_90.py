from src.bingo import carton

def test_uno_a_noventa():
    mi_carton = carton()
    contador = 0

    for fila in range(0, 3):
        for columna in range(0, 9):
           celda = mi_carton[fila][columna]
           assert celda >= 0 and celda <= 90
