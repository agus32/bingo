from src.bingo import carton

def test_no_mayor():
    mi_carton = carton()
    contador = 0
    lleno=0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
        if contador > 0:
            lleno = lleno+1    
    # Esperamos encontrar 3 filas no vacias
    assert lleno == 3
