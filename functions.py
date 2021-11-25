# Neede functions

import copy
from random import randint
from population import *


def checkNeighbor(indi,popu):
    x = indi.coord_x-3
    scoreVecino = 0
    conta = 0
    while x <= indi.coord_x+3:
        y = indi.coord_y-3
        while y <= indi.coord_y+3:
                for i in popu:
                    if i != indi:
                        if i.coord_x == x and i.coord_y == y and i.adap_score != 0 and indi.adap_score != 0:
                            scoreVecino += 25
                            conta += 1
                y += 1
        x += 1
    if conta > 0 and scoreVecino > 0:
        print("AUMENTO, POR VECINOS",indi.coord_x,indi.coord_y, "Puntaje", scoreVecino, "Cantida de vecinos", conta)               
        indi.set_score(indi.adap_score + scoreVecino)


def checkWalls(ind,img):
    x = ind.coord_x
    y = ind.coord_y
    score = ind.adap_score
    pt = 0
    try:
        x += 3 # 3 a la derecha
        if img[x,y][0] == 0 and img[x,y][1] == 0 and img[x,y][2] == 0: #Revisar que sea pixel negro
                pt += 1
        x -= 6 # 3 a la izquierda de donde inicia
        if img[x,y][0] == 0 and img[x,y][1] == 0 and img[x,y][2] == 0: #Revisar que sea pixel negro
                pt += 1

        x += 3 #Reajusta el valor a donde estaba

        y += 3 # 3 a la arriba
        if img[x,y][0] == 0 and img[x,y][1] == 0 and img[x,y][2] == 0: #Revisar que sea pixel negro
                pt += 1
        y -= 6 # 3 a la abajo de donde inicia
        if img[x,y][0] == 0 and img[x,y][1] == 0 and img[x,y][2] == 0: #Revisar que sea pixel negro
                pt += 1
    except:
        return
    if (pt == 0):
        score = score * 1  
    if (pt == 1):
        score = score * 0.75
    if (pt == 2):
        score = score * 0.50
    if (pt == 3):
        score = score * 0.25
    
    if score > 0:
        print("AUMENTO POR PAREDES",ind.coord_x,ind.coord_y, "Puntaje", score)
        ind.set_score(ind.adap_score + score)


#Cuando se llame a fitness tiene que ser con un allPopulation
def fitness(popu,laberinto):
      puntaje = 0
      for i in popu:
            if i.getColor == 0:
                 puntaje = checkNeighbor(i,popu)
                 puntaje = checkWalls(i,puntaje,laberinto)
                 i.set_score(puntaje)
      return popu