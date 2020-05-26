from src.bingo import carton

def test_3x9():
    mi_carton = carton()
    assert len(mi_carton) == 3
    assert len(mi_carton[0]) == 9
    assert len(mi_carton[1]) == 9
    assert len(mi_carton[2]) == 9
