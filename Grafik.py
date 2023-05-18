import pandas as pd
import random
from Converter import *

chromosome = ['A', 'B', 'C', 'D', 'E', 'B', 'E', 'D', 'E', 'E', 'E', 'A', 'C', 'D', 'H', 'C', 'D', 'E', 'B', 'C', 'B']

def evaluate_fitness(chromosome):
    fitness = 0
    for a in antipreferences:
        if a[0] == chromosome[int(a[1])]:
            fitness += 1
    for p in preferences:
        if p[0] == chromosome[int(p[1])]:
            fitness -= 1
    for d in range(len(chromosome)-1):
        if chromosome[d] == chromosome[d + 1]:
            fitness +=1        
    return fitness

print(evaluate_fitness(chromosome))
