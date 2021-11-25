#libs
import copy
from random import randint
from individual import *


# Class for the total population of individuals
class population:
    #Attributes
    all_population = []

    #Init - listado con valores iniciales
    def __init__(self, cant):
        while ( len(self.all_population)!=cant ):

            #get random point
            x = randint(0,49)
            y = randint(0,49)
            new_individual = individual(x,y)

            #Evaluar inicial case
            if len(self.all_population)==0:
                self.add_individual(new_individual)
            else:
                #validar que punto no exista
                exists = False
                for i in self.all_population:
                    if ( (i.coord_x==x) and (i.coord_y==y) ):
                        exists = True

                #determinar si el punto se añade
                if not exists:
                    self.add_individual(new_individual)
        

    #Methods
            #add un individuo
    def add_individual(self, individual):
        self.all_population.append(individual)


            #Cruce de cromosomas
    def cross(self):
        for indi in self.all_population:
            #get random point
            pos_1 = randint(0,len(self.all_population)-1)

            #get individuals
            ind_1 = copy.deepcopy(self.all_population[pos_1])

            # si la adaptabilidad del individuo es menor al aleatorio
            if indi.adap_score>ind_1.adap_score:

                #Evaluar cual cromosoma mutar
                x_y = randint(0,1)

                if x_y==0:#Cruzar cromosoma x
                    ind_1.coord_x = indi.coord_x

                else:#Cruzar cromosomas y
                    ind_1.coord_y = indi.coord_y


                #validar que puntos no existan
                exists = False
                for i in self.all_population:
                    if ( (i.coord_x==ind_1.coord_x) and (i.coord_y==ind_1.coord_y) ):
                        exists = True

                #determinar si el punto se añade
                if not exists:
                    self.all_population[pos_1] = copy.deepcopy(ind_1)

        #Mutar un cromosoma
    def mutate(self):
        for individuo in self.all_population:
            mut_ind = copy.deepcopy(individuo)
            #Determinar si se muta
            proba_aleatoria = randint(0,101)
            if proba_aleatoria <= mut_ind.probabilidad:
                
                #Determinar valor de mutacion
                mut_gen = randint(0,49)
                x_y = randint(0,1)

                #Evaluar cual cromosoma mutar
                if x_y==0:#mutar x
                    mut_ind.coord_x = mut_gen

                else:#mutar y
                    mut_ind.coord_y = mut_gen

                #validar que punto no exista
                exists = False
                for i in self.all_population:
                    if ( (i.coord_x==mut_ind.coord_x) and (i.coord_y==mut_ind.coord_y) ):
                        exists = True

                #determinar si el punto se añade
                if not exists:
                    individuo = mut_ind


    def checkNeighbor(self):
        for indi in self.all_population:
            x = indi.coord_x-3
            scoreVecino = 0
            conta = 0
            while x <= indi.coord_x+3:
                y = indi.coord_y-3
                while y <= indi.coord_y+3:
                        for i in self.all_population:
                            if i != indi:
                                if i.coord_x == x and i.coord_y == y and i.adap_score != 0 and indi.adap_score != 0:
                                    scoreVecino += 25
                                    conta += 1
                        y += 1
                x += 1
            if conta > 0 and scoreVecino > 0:
                print("AUMENTO, POR VECINOS",indi.coord_x,indi.coord_y, "Puntaje", scoreVecino, "Cantida de vecinos", conta)               
                indi.set_score(indi.adap_score + scoreVecino)


    def checkWalls(self,img):
        for ind in self.all_population:
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


        # carcular la probabilidad de seleccion de un individuo
    def selection(self):
        for individio in self.all_population:
            color = individio.color

            #establecer probabilidades
            if color[0]==0 and color[1]==0 and color[2]==0:         #color negro
                individio.probabilidad = 20
                
            elif color[0]==255 and color[1]==255 and color[2]==255: #color blanco
                individio.probabilidad = 0
                
            elif color[0]==0 and color[1]==255 and color[2]==0:     #color verde
                individio.probabilidad = 5

            elif color[0]==255 and color[1]==0 and color[2]==0:     #color azul
                individio.probabilidad = 5


        # Cuando se llame a fitness tiene que ser con un allPopulation
    def fitness(self,img):
            # Check Walls and Neighbors. This functions sets the idividua adap_score
        self.checkWalls(img)
        self.checkNeighbor()

            # Determinar selection. Sets probabilidad de seleccion de individuos
        self.selection()



            #print toda la lista de población
    def print(self):
        print(" ")
        print("           POBLACION")
        print("---------------------------------------")
        print("x      y      adap       prob     color")
        print("---------------------------------------")
        for i in self.all_population:
            print("%d     %d     %d         %d      [%d,%d,%d]" % (i.coord_x,i.coord_y,i.adap_score,i.probabilidad,i.color[0],i.color[1],i.color[2]))
        print("---------------------------------------")
        print(" ")


















        
