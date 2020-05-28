import random
import math
def intentoCarton():
    contador = 0
    carton = (
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    )
    numerosCarton = 0

    while (numerosCarton < 15):
      contador = contador + 1
      if (contador == 50):
        return intentoCarton()
      numero = random.randint(1,90)

      columna = math.floor(numero / 10)
      if (columna == 9):
          columna = 8
      huecos = 0
      for i in range(3):
        if (carton[i][columna] == 0):
          huecos = huecos + 1
        if (carton[i][columna] == numero):
          huecos = 0
          break
      if (huecos < 2):
        continue
      fila = 0
      for j in range(3):
        huecos = 0
        for i in range(9):
          if (carton[fila][i] == 0):
              huecos = huecos + 1
        if (huecos < 5 or carton[fila][columna] != 0):
          fila = fila + 1
        else:
          break
      if (fila == 3):
        continue
      carton[fila][columna] = numero
      numerosCarton = numerosCarton + 1
      contador = 0
    for x in range(9):
      huecos = 0
      for y in range(3):
        if (carton[y][x] == 0):
            huecos = huecos + 1
      if (huecos == 3):
        return intentoCarton()
    return carton

def imprimirCarton(carton):
    for columna in range(3):
        for fila in range(9):
            print(carton[columna][fila], end = " ")
        print('\n')



def carton():
    while(True):
        carton1 = intentoCarton()
        if  tres_columnas_1celda(carton1) == True and  cinco_celdasxfila(carton1) == True and  columnas_no_llenas(carton1) == True and  arriba_abajo(carton1) == True and  nomas_2celdas_llenas_cons(carton1) == True and  nomas_2celdas_vacias_cons(carton1) == True and  no_repetido(carton1) == True:
            return carton1;



def tres_columnas_1celda(mi_carton):
    celda_vacia = 0
    contador = 0
    columna_de_1 = 0
    result = True
    for columna in range(0, 9):
        for fila in range(0, 3):
            if mi_carton[fila][columna] != celda_vacia:
                contador = contador + 1
        if contador == 1:
            columna_de_1 = 1 + columna_de_1
        contador = 0
    if columna_de_1 != 3:
      result = False
    return result

def cinco_celdasxfila(mi_carton):
    celda_vacia = 0
    contador = 0
    result = True
    for fila in range(0, 3):
        for columna in range(0, 9):
            if mi_carton[fila][columna] != celda_vacia:
                contador = contador+1
        if contador != 5:
          result = False
        contador = 0
    return result

def columnas_no_llenas(mi_carton):
    celda_vacia = 0
    contador = 0
    result = True
    for columna in range(0, 9):
        for fila in range(0, 3):
            if mi_carton[fila][columna] != celda_vacia:
                contador = contador + 1
        if contador == 3:
          result = False
        contador = 0
    return result

def arriba_abajo(mi_carton):
    celda_vacia = 0
    j = 0
    contador = 0
    result = True
    for j in range(9):

        if mi_carton[1][j] != celda_vacia:
     	    if mi_carton[0][j] > mi_carton[1][j]:
             result = False

        if mi_carton[2][j] != celda_vacia:
     	    if mi_carton[1][j] > mi_carton[2][j] or mi_carton[0][j] > mi_carton[2][j]:
             result = False
    return result


def nomas_2celdas_llenas_cons(mi_carton):
    celda_vacia = 0
    contador = 0
    result = True
    for fila in range(0, 3):
        for columna in range(0, 9):
            if mi_carton[fila][columna] != celda_vacia:
                contador = contador+1
            else:
                if contador > 2 :
                  result = False
                contador = 0
        contador = 0
    return result

def nomas_2celdas_vacias_cons(mi_carton):
    celda_vacia = 0
    contador = 0
    result = True
    for fila in range(0, 3):
        for columna in range(0, 9):
            if mi_carton[fila][columna] == celda_vacia:
                contador = contador+1
            else:
                if contador > 2 :
                  result = False
                contador = 0
        contador = 0
    return result


def no_repetido(mi_carton):
    lista_carton = mi_carton[0] + mi_carton[1] + mi_carton[2]
    if len(set(lista_carton)) != 16:
      return False
    else:
      return True 


