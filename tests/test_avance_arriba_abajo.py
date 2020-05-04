from src.bingo import carton

def test_arriba_abajo():
    mi_carton = (
	(0,15,0,31,40,0,61,0,85),
	(1,0,27,0,45,53,0,77,0),
	(5,0,0,37,0,59,66,0,87)
    )
    celda_vacia = 0
    j = 0
    contador = 0
    for j in range(9):

        if mi_carton[1][j] != celda_vacia:
     	    assert mi_carton[0][j] < mi_carton[1][j]

        if mi_carton[2][j] != celda_vacia:
     	    assert mi_carton[1][j] < mi_carton[2][j] and mi_carton[0][j] < mi_carton[2][j]
