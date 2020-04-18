from src.bingo import carton

def test_columna():
    mi_carton = carton()
    j = 0
    contador=0 
    for j in range(9):
        suma= sum([fila[j] for fila in mi_carton])
        if suma > 0:
            contador = contador+1
# contador suma 1 por cada columna no vacia 
    assert contador == 9
