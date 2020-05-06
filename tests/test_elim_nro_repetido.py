from src.bingo import carton

def test_arriba_abajo():
    mi_carton = (
	(0,15,0,31,40,0,61,0,85),
	(1,0,27,0,45,53,0,77,0),
	(5,0,0,37,0,59,66,0,87)
    )
    lista_carton = mi_carton[0] + mi_carton[1] + mi_carton[2]
    assert len(set(lista_carton)) == 16
