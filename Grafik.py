import pandas as pd
import random
from Converter import *

chromosome =  [['A', 'B', 'C'], ['D', 'E', 'F'], ['G'], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G'], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G'], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G'], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G'],]

def evaluate_fitness(chromosome):
    fitness = 0
    for a in antipreferences:
        if a[0] in chromosome[int(a[1])]:
            fitness += 1
    for p in preferences:
        if p[0] in chromosome[int(p[1])]:
            fitness -= 1
    for d in range(len(chromosome)-1):
        for el in chromosome[d]:
            if el in chromosome[d+1]:
                fitness += 2
    for d in range(len(chromosome)-2):
        for el in chromosome[d]:
            if el in chromosome[d+2]:
                fitness += 1
    for x in chromosome:
        if len(x) != len(set(x)):
            fitness += 5
    print(fitness)
    return fitness

evaluate_fitness(chromosome)


