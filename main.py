import numpy as np
import random as rand
import sys
from Mutation import mutation
from Crossover import crossover
from Selection import selection

Ud = sys.argv[1]
population = sys.argv[2]
dim = sys.argv[3]
F = sys.argv[4]
CR = sys.argv[5]
iteration = sys.argv[6]

Ld = float(Ud) * (-1)

# Initial 
populationDataOriginal = np.zeros((int(population), int(dim)))
for eachpopulationData_colum in range(int(population)):
    for eachpopulationData_row in range(int(dim)):
        r = rand.random()
        populationDataOriginal[eachpopulationData_colum][eachpopulationData_row] = ((float(Ud) - Ld) * r) + Ld
populationData = populationDataOriginal.copy() # copy populationDataOriginal to populationData

for i in range(int(iteration)):
	# Mutation
	mutationData = mutation(populationData, float(F))

	# Crossover
	crossoverData = crossover(populationDataOriginal, mutationData, float(CR))

	# Selection
	selectionData = selection(populationDataOriginal, crossoverData, int(dim))			
	
	# reset
	populationDataOriginal = selectionData.copy()
	populationData = selectionData.copy()