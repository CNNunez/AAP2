
#libs
import cv2
import numpy as np
import os
from population import *
from functions import *
from laberintos import *
#from PIL import Image

"""
3 2
28 2
1 2 

x = 0
new_population = population(10) # Get first generation
new_population.print()
while (x == 0):
    x = new_population.mutate()

print('Muto algo')
new_population.print()

,score,lab

new_population = population(10) # Get first generation
new_population.print()
for i in range(10):
    print(checkWalls(new_population.all_population[i]))

    l.evolve()
l.print(1)

checkWalls(l.record_population[0].all_population[0])

for i in l.record_population[0].all_population:
    checkNeighbor(i,l.record_population[0].all_population)

l.evolve()
l.print(2)
"""

l = laberintos("IMGs",1)
l.print(0)
l.evolve()
for i in l.record_population[0].all_population:
    checkWalls(i,l.record_laberintos[0])
    checkNeighbor(i,l.record_population[0].all_population)
l.print(1)







