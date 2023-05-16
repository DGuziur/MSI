import random

number_of_iterations = 500
number_of_parents = 3
work_shifts = 21
mutate_percent = 50
pracownicy = [1, 2, 3, 4, 5]
population = []

def create_starting_population(e):
    for x in range(e):
        chromosome = []
        for x in range(work_shifts):
            chromosome.append(random.choice(pracownicy))
        population.append(chromosome)

def evaluate_fitness(chromosome):
    fitness = 0
    for i in range(len(chromosome)-1):
      if chromosome[i] == chromosome[i + 1]:
        fitness +=1
    print(f"Fitness = {str(fitness)}")
    return fitness

create_starting_population(number_of_parents)

for chromosome in population:
   evaluate_fitness(chromosome)

print(population)

def keep_population_at_10(population):
    if len(population) > 10:
        population.remove(max(population, key=evaluate_fitness))
        keep_population_at_10(population)
    else: print(population)

def mutate(chromosome):
    if mutate_percent <= random.randint(1,100):
        mutated_gene = random.randint(0, 20)
        mutation = random.choice(pracownicy)
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

naj = min(population, key=evaluate_fitness)
print("Naj wynik: ")
evaluate_fitness(naj)
print(naj)