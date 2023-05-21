import pandas as pd
import random
from Converter import *
population = []

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
    print(fitness)   
    return fitness

chromosome1 = [['E', 'H', 'A'], ['B', 'C', 'D'], ['C'], ['B', 'C', 'H'], ['H', 'D', 'B'], ['E'], ['A', 'A', 'F'], ['E', 'G', 'C'], ['C'], ['B', 'H', 'H'], ['C', 'D', 'A'], ['F'], ['G', 'D', 'F'], ['G', 'F', 'E'], ['B']]
chromosome2 = [['G', 'G', 'C'], ['G', 'F', 'B'], ['A'], ['G', 'F', 'E'], ['G', 'D', 'F'], ['G'], ['A', 'B', 'G'], ['D', 'C', 'F'], ['B'], ['D', 'C', 'C'], ['A', 'C', 'A'], ['D'], ['E', 'D', 'E'], ['G', 'C', 'C'], ['E']]
def crossover(parent1, parent2):
    pop = []
    for el in population:
        pop.append(evaluate_fitness(el))
    print(f'Crossover{pop}')
    split_point = random.randint(1, 14)
    child1 = parent1[:split_point] + parent2[split_point:]
    child2 = parent2[:split_point] + parent1[split_point:]
    population.append(child1)
    print(child1)
    print(child2)
    pop = []
    for el in population:
        pop.append(evaluate_fitness(el))
    print(f'PostCrossover{pop}')

crossover(chromosome1, chromosome2)