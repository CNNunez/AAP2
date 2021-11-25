#libs
from population import *
from functions import *
from laberintos import *




# Get laberintos de prueba
l = laberintos("IMGs",4)
for i in range(15):
    l.evolve(i+1)
    #input()

