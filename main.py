#libs
from population import *
from functions import *
from laberintos import *




# Get laberintos de prueba
l = laberintos("IMGs",1)
for i in range(10):
    l.evolve()
    input()


#print results
for i in range(l.length()):
    l.print(i)
    input()
