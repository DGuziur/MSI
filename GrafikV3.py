import random
import pandas as pd
import re
import time
from Converter import *
import copy

population = []
work_shifts = ["pn-1","pn-2","pn-3","wt-1","wt-2","wt-3","sr-1","sr-2",
               "sr-3","czw-1","czw-2","czw-3","pt-1","pt-2","pt-3"]

df1 = pd.DataFrame(columns=["pn-1","pn-2","pn-3","wt-1","wt-2","wt-3","sr-1","sr-2",
                            "sr-3","czw-1","czw-2","czw-3","pt-1","pt-2","pt-3","fitness"])

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
        if len(x) != len(set(x)):
            fitness += 5
    print(fitness)
    return fitness

def kill_the_weak(population):
    while len(population) > 10:
        population.remove(max(population, key=evaluate_fitness))

def tournament_selection(population):
    selected = []
    for i in range(len(population)):
        contestants = random.sample(population, 2)
        winner = min(contestants, key=evaluate_fitness)
        selected.append(winner)
    for el in range(len(selected) - 1):
        crossover(selected[el], selected[el + 1])

def crossover(parent1, parent2):
    split_point = random.randint(1, len(work_shifts) - 1)
    mutate(parent1[:split_point] + parent2[split_point:])
    mutate(parent2[:split_point] + parent1[split_point:])

def mutate(child):
    child = copy.deepcopy(child)
    if mutate_percent <= random.randint(1,100):
         for i in range(random.randint(1, 2)):
            emp = copy.deepcopy(employees)
            mutated_gene = random.randint(0, len(work_shifts) - 1)
            for el in set(child[mutated_gene]):
                emp.remove(el)
            mutation = random.choice(child[mutated_gene])
            child[mutated_gene][child[mutated_gene].index(mutation)] = random.choice(emp)
    population.append(child)

create_starting_population(number_of_parents)

for i in range(number_of_iterations):
    tournament_selection(population)
    kill_the_weak(population)
    for el in population:
        df2 = pd.DataFrame([[el[0],el[1],el[2],el[3],el[4],el[5],el[6],el[7],el[8],el[9],
                             el[10],el[11],el[12],el[13],el[14],evaluate_fitness(el)]],
                   index=[i + 1],
                   columns=["pn-1","pn-2","pn-3","wt-1","wt-2","wt-3","sr-1","sr-2",
                            "sr-3","czw-1","czw-2","czw-3","pt-1","pt-2","pt-3","fitness"])
        df1 = pd.concat([df1, df2])
        
df1.to_excel("Wynik.xlsx")
print(f"Wynik: {min(population, key=evaluate_fitness)}")