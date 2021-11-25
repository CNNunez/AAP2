# Neede functions

import copy
from random import randint
from population import *

def checkWalls(indi,popu):
    return 0


def checkNeighbor(indi,popu):
    x = indi.coord_x-3
    puntaje = 0
    conta = 0
    while x < indi.coord_x+3:
        y = indi.coord_y-3
        while y != indi.coord_y+3:
                for i in popu:
                    if i != indi:
                        if i.coord_x == x and i.coord_y == 2:
                            print("listo",i.coord_x,i.coord_y)
                            indi.set_color([100,255,100])
                            #puntaje = puntaje + i.getPuntaje()
                            conta += 1
                y += 1
        x += 1
    if conta!=0:
        return puntaje/conta
    return (x,y)


def checkWalls(ind,img):
    x = ind.coord_x
    y = ind.coord_y
    score = ind.adap_score
    pt = 0
    try:
        x += 3 # 3 a la derecha
        if img[y,x][0] != 255 and img[y,x][1] != 255 and img[y,x][2] != 255:
                pt += 1
        x -= 6 # 3 a la izquierda de donde inicia
        if img[y,x][0] != 255 and img[y,x][1] != 255 and img[y,x][2] != 255:
                pt += 1

        x += 3 #Reajusta el valor a donde estaba

        y += 3 # 3 a la arriba
        if img[y,x][0] != 255 and img[y,x][1] != 255 and img[y,x][2] != 255:
                pt += 1
        y -= 6 # 3 a la abajo de donde inicia
        if img[y,x][0] != 255 and img[y,x][1] != 255 and img[y,x][2] != 255:
                pt += 1
    except:
        return
    if (pt == 0):
        score *= 2   
    if (pt == 1):
        score *= 1.75
    elif (pt == 2):
        score *= 1.50
    elif (pt == 3):
        score *= 1.25

    ind.set_score(score)


#Cuando se llame a fitness tiene que ser con un allPopulation
def fitness(popu,laberinto):
      puntaje = 0
      for i in popu:
            if i.getColor == 0:
                 puntaje = checkNeighbor(i,popu)
                 puntaje = checkWalls(i,puntaje,laberinto)
                 i.set_score(puntaje)
      return popu