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
    def __init__(self, folder_name, cant,cantIndi):
        path = folder_name + "/" + str(cant) + ".png"
        new_img = cv2.imread(path)    # Read laberinto
        new_population = population(cantIndi) # Get first generation

        # save data
        self.record_laberintos.append(new_img)
        self.record_population.append(new_population)
        self.set_color()
        self.add_record(new_population)
        self.check_white()
        
        # update colors
        self.set_color()
        self.print(0)
        

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
        img = self.record_laberintos[position+1]
        scale = 5 # times of original size
        dim = (int(img.shape[1] * scale), int(img.shape[0] * scale))
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        #path = 'C:/Users/Carolina/Documents/TEC/2021/AA/Proyecto 2/AAP2/Results/Imag' + str(position) + '.png'
        path = os.path.dirname(os.path.realpath(__file__))+'\\Results\\Imagen' + str(position) + '.png'
        cv2.imwrite(path, resized)
        self.record_population[position+1].print()


            #paint population track
    def paint(self, population):
        img = copy.deepcopy(self.record_laberintos[0])
        img[0,0] = (255,255,255)
        img[25,25] = (255,0,255)
        for individual in population.all_population:
            #get data
            x = individual.coord_x
            y = individual.coord_y
            #change pixel color
            img[x,y] = (0,0,255)
        return img


            # Set individuals colors
    def set_color(self):
        last_population = self.record_population[ len(self.record_population)-1 ]
        img = self.record_laberintos[0]
        for individual in last_population.all_population:
            x = individual.coord_x
            y = individual.coord_y

            # get and set pixel color
            pixel_color = img[x, y]
            individual.set_color(pixel_color)

        
            #evolucionar la poblacion
    def evolve(self,num):   #num es numero de evolucion
        print(" ")
        print(" ")
        print("             Evolucion #%d"%(num))
        print("---------------------------------------")
        self.check_white()
        evo_population = copy.deepcopy(self.record_population[ len(self.record_population)-1 ])

        # Do fitness
        evo_population.fitness(self.record_laberintos[0])
        
        evo_population.cross()
        evo_population.mutate()
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


        self.set_color()

        #print results
        self.print(num)
        


    #Revisa que el punto este en un camino
    def check_white(self):
        img = copy.deepcopy(self.record_laberintos[0])
        for individual in self.record_population[ len(self.record_population)-1 ].all_population:
            #get data
            x = individual.coord_x
            y = individual.coord_y
            #change pixel color
            b,g,r = (img[x, y])
            if (b == 255 and g == 255 and r == 255):
                individual.set_score(50)
            elif (b == 0 and g == 255 and r == 0):
                individual.set_score(25)
            elif (b == 255 and g == 0 and r == 0):
                individual.set_score(25)
            elif (b == 0 and g == 0 and r == 0):
                individual.set_score(0)
    
