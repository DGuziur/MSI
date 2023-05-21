import random
import pandas as pd
import re
import time
from Converter import *

population = []
work_shifts = ["pn-1","pn-2","pn-3","wt-1","wt-2","wt-3","sr-1","sr-2",
               "sr-3","czw-1","czw-2","czw-3","pt-1","pt-2","pt-3"]

df1 = pd.DataFrame(columns=["osobnik","fitness"])

def create_starting_population(i):
    for x in range(i):
        chromosome = []
        for x in range(len(work_shifts)):
            day = []
            if re.compile(".+-[1-2]").match(work_shifts[x]):
                day.append(random.choice(employees))
                day.append(random.choice(employees))
                day.append(random.choice(employees))
            if re.compile(".+-[3]").match(work_shifts[x]):
                day.append(random.choice(employees))
            chromosome.append(day)
        population.append(chromosome)

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
        if x != set(x):
            fitness += 5
    return fitness

def kill_the_weak(population):
    while len(population) > 10:
        population.remove(max(population, key=evaluate_fitness))

def tournament_selection(population):
    selected = []
    pop = []
    for el in population:
        pop.append(evaluate_fitness(el))
    print(f'Tournament{pop}')
    for i in range(len(population)):
        contestants = random.sample(population, 2)
        winner = min(contestants, key=evaluate_fitness)
        selected.append(winner)
    for el in range(len(selected) - 1):
        crossover(selected[el], selected[el + 1])

def crossover(parent1, parent2):
    population.remove(parent1)
    population.remove(parent2)
    pop = []
    for el in population:
        pop.append(evaluate_fitness(el))
    print(f'Crossover{pop}')
    split_point = random.randint(1, len(work_shifts) - 1)
    child1 = parent1[:split_point] + parent2[split_point:]
    child2 = parent2[:split_point] + parent1[split_point:]
    child1 = mutate(child1)
    child2 = mutate(child2)
    population.append(child1)
    population.append(child2)
    pop = []
    for el in population:
        pop.append(evaluate_fitness(el))
    print(f'PostCrossover{pop}')

def mutate(child):
    child = child.copy()
    if mutate_percent <= random.randint(1,100):
        for i in range(random.randint(1, 10)):
            day = random.randint(0, len(child)-1)
            gene = random.randint(0, len(child[day])-1)
            mutation = random.choice(employees)
            child[day][gene] = mutation
    return child

create_starting_population(number_of_parents)

for i in range(number_of_iterations):
    tournament_selection(population)
    kill_the_weak(population)
