#libs
from population import *
from functions import *
from laberintos import *




# Get laberintos de prueba
l = laberintos("IMGs",4,100)
for i in range(50):
    l.evolve(i+1)
    #input()

