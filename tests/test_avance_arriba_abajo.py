from src.bingo import carton

def test_arriba_abajo():
    mi_carton = carton()
    celda_vacia = 0
    j = 0
    contador = 0
    for j in range(9):

        if mi_carton[1][j] != celda_vacia:
     	    assert mi_carton[0][j] < mi_carton[1][j]

        if mi_carton[2][j] != celda_vacia:
     	    assert mi_carton[1][j] < mi_carton[2][j] and mi_carton[0][j] < mi_carton[2][j]
