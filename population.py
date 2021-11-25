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
        #get random point
        pos_1 = randint(0,len(self.all_population)-1)
        pos_2 = randint(0,len(self.all_population)-1)

        #get individuals
        ind_1 = self.all_population[pos_1]
        ind_2 = self.all_population[pos_2]

        #Cruzar cromosomas
        new_1 = individual(ind_1.coord_x,ind_2.coord_y)
        new_2 = individual(ind_2.coord_x,ind_1.coord_y)

        #validar que puntos no existan
        exists = False
        for i in self.all_population:
            if ( (i.coord_x==new_1.coord_x) and (i.coord_y==new_1.coord_y) ):

                for j in self.all_population:
                    if ( (j.coord_x==new_2.coord_x) and (j.coord_y==new_2.coord_y) ):
                        exists = True

        #determinar si el punto se añade
        if not exists:
            self.all_population[pos_1] = new_1
            self.all_population[pos_2] = new_2
        

        #Mutar un cromosoma
    def mutate(self):
        #get random mutation data
        mut_pos = randint(0,len(self.all_population)-1)
        mut_ind = copy.deepcopy(self.all_population[mut_pos])      #deberia heredar adap y color????
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
            self.all_population[mut_pos] = mut_ind

        
            #print toda la lista de población
    def print(self):
        print(" ")
        print("           POBLACION")
        print("------------------------------")
        print("x      y      adap       color")
        print("------------------------------")
        for i in self.all_population:
            print("%d     %d     %d     [%d,%d,%d]" % (i.coord_x,i.coord_y,i.adap_score,i.color[0],i.color[1],i.color[2]))
        print("------------------------------")
        print(" ")


















        
