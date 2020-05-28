from src.bingo import carton

def test_elim_nro_rep():
    mi_carton = carton()
    lista_carton = mi_carton[0] + mi_carton[1] + mi_carton[2]
    assert len(set(lista_carton)) == 16
