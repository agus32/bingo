from src.bingo import carton

def test_izq_der():
    mi_carton = (
	(0,15,0,31,40,0,61,0,85),
	(1,0,27,0,45,53,0,77,0),
	(5,0,0,37,0,59,66,0,87)
    )
    celda_vacia = 0
    contador = 0
    for fila in range(0, 3):
        for columna in range(1, 9):
            if mi_carton[fila][columna] != celda_vacia:
                assert mi_carton[fila][columna-1] < mi_carton[fila][columna]
