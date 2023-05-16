import random
import pandas as pd

number_of_iterations = 50
number_of_parents = 100
work_shifts = 21
mutate_percent = 50
employees = [1, 2, 3, 4, 5, 6]
population = []

df1 = pd.DataFrame(columns=["osobnik","fitness"])

def create_starting_population(e):
    for x in range(e):
        chromosome = []
        for x in range(work_shifts):
            chromosome.append(random.choice(employees))
        population.append(chromosome)

def evaluate_fitness(chromosome):
    fitness = 0
    for i in range(len(chromosome)-1):
      if chromosome[i] == chromosome[i + 1]:
        fitness +=1
    if chromosome[0] != 1:
        fitness += 1
    if chromosome[20] != 2:
        fitness += 1
    print(f"Fitness = {str(fitness)}")
    return fitness

create_starting_population(number_of_parents)

for chromosome in population:
   df2 = pd.DataFrame([[chromosome, evaluate_fitness(chromosome)]],
                   index=[00],
                   columns=["osobnik","fitness"])
   df1 = pd.concat([df1, df2])

print(population)

def keep_population_at_10(population):
    if len(population) > 10:
        population.remove(max(population, key=evaluate_fitness))
        keep_population_at_10(population)
    else: print(population)

def mutate(chromosome):
    if mutate_percent <= random.randint(1,100):
        mutated_gene = random.randint(0, 20)
        mutation = random.choice(employees)
        chromosome[mutated_gene] = mutation
        

def crossover(parent1, parent2):
    split_point = random.randint(1, 20)
    child1 = parent1[:split_point] + parent2[split_point:]
    child2 = parent2[:split_point] + parent1[split_point:]
    mutate(child1)
    mutate(child2)
    population.append(child1)
    population.append(child2)


def tournament_selection(population):
    selected = []
    for i in range(len(population)):
        contestants = random.sample(population, 2)
        winner = min(contestants, key=evaluate_fitness)
        selected.append(winner)
    print(selected)
    for el in range(len(selected) - 1):
        crossover(selected[el], selected[el + 1])
    print("Nowa Populacja:")
    print(population)
    print("Nowa Populacja but at 10:")
    keep_population_at_10(population)
    
       

for i in range(number_of_iterations):
    tournament_selection(population)
    for el in population:
        df2 = pd.DataFrame([[el, evaluate_fitness(el)]],
                   index=[i + 1],
                   columns=["osobnik","fitness"])
        df1 = pd.concat([df1, df2])
    

naj = min(population, key=evaluate_fitness)
print("Naj wynik: ")
evaluate_fitness(naj)
print(naj)

df3 = pd.DataFrame([[naj]],
                   index=["naj"],
                   columns=["najlepszy"])
df1 = pd.concat([df3, df1])
df1.to_excel("Wynik.xlsx")