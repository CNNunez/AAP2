#libs
import cv2
import numpy as np
import os
from population import *
#from PIL import Image


# Class con todas las imagenes de prueba
class laberintos:
    #Attributes
    record_laberintos = []
    record_population = []
    

    #Init
    def __init__(self, folder_name, cant):
        path = folder_name + "/" + str(cant) + ".png"
        new_img = cv2.imread(path)    # Read laberinto
        new_population = population(50) # Get first generation
        self.record_laberintos.append(new_img)
        self.record_population.append(new_population)
        self.chec_white(self.record_population[0])
    
    #Methods
            #return length
    def length(self):
        return len(self.record_population)
    
            #add un laberinto
    def add_record(self,populatio):
        self.record_laberintos.append(self.paint(population))
        self.record_population.append(populatio)

            #print imagen y su poblacion
    def print(self,position):
        img = self.record_laberintos[position]
        scale = 5 # times of original size
        dim = (int(img.shape[1] * scale), int(img.shape[0] * scale))
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        path = os.path.dirname(os.path.realpath(__file__))+'\\Results\\Imagen' + str(100+position) + '.png'
        cv2.imwrite(path, resized)
        self.record_population[position].print()

            #paint population track
    def paint(self, population):
        img = copy.deepcopy(self.record_laberintos[0])
        for individual in population.all_population:
            #get data
            x = individual.coord_x
            y = individual.coord_y
            #change pixel color
            img[x,y] = individual.color
        return img


            #evolucionar la poblacion
    def evolve(self):
        evo_population = copy.deepcopy(self.record_population[ len(self.record_population)-1 ])
        evo_population.cross()
        self.add_record(evo_population)

    #Revisa que el punto este en un camino
    def chec_white(self, population):
        img = copy.deepcopy(self.record_laberintos[0])
        for individual in population.all_population:
            #get data
            x = individual.coord_x
            y = individual.coord_y
            #change pixel color
            b,g,r = (img[x, y])
            if (b == 255 and g == 255 and r == 255):
                individual.set_score(50)
            if (b == 0 and g == 255 and r == 0):
                individual.set_score(0)


        


    
