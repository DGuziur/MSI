import random
from tabulate import tabulate

# Ustawienie parametrów algorytmu
NUM_WORKERS = 10  # Liczba pracowników
NUM_HOURS = 8  # Liczba godzin pracy w ciągu dnia
MIN_HOURS = 2  # Minimalna liczba godzin pracy
WORK_HOURS = list(range(10, 20))  # Dostępne godziny pracy
TABU_DAY = 4  # Dzień tygodnia, który nie jest dostępny dla pracowników

# Ustawienie preferencji i wymagań pracowników
PREFERENCES = {
    0: [10, 11, 12, 13, 14],  # Preferowane godziny pracy dla pracownika 0
    1: [15, 16, 17, 18, 19],  # Preferowane godziny pracy dla pracownika 1
    # ...
}
REQUIREMENTS = {
    0: [10, 11, 12, 13, 14],  # Wymagane godziny pracy dla pracownika 0
    1: [15, 16, 17, 18, 19],  # Wymagane godziny pracy dla pracownika 1
    # ...
}

# Inicjalizacja populacji początkowej
def generate_population(size):
    population = []
    for i in range(size):
        chromosome = []
        for j in range(NUM_WORKERS):
            hours = random.sample(WORK_HOURS, MIN_HOURS)
            while sum(hours) < NUM_HOURS:
                hour = random.choice(WORK_HOURS)
                if hour not in hours:
                    hours.append(hour)
            chromosome.append(hours)
        population.append(chromosome)
    return population

# Obliczenie wartości funkcji celu dla chromosomu
def evaluate_chromosome(chromosome):
    score = 0
    for i in range(NUM_WORKERS):
        hours = chromosome[i]
        if TABU_DAY in hours:
            return 0
        if set(hours).intersection(PREFERENCES[i]):
            score += 1
        if not set(REQUIREMENTS[i]).issubset(set(hours)):
            return 0
    return score

# Selekcja chromosomów za pomocą turnieju dwóch osobników
def tournament_selection(population, size):
    selected = []
    for i in range(size):
        contestants = random.sample(population, 2)
        winner = max(contestants, key=evaluate_chromosome)
        selected.append(winner)
    return selected

# Krzyżowanie chromosomów za pomocą punktu przecięcia
def crossover(parent1, parent2):
    split_point = random.randint(1, NUM_WORKERS - 1)
    child1 = parent1[:split_point] + parent2[split_point:]
    child2 = parent2[:split_point] + parent1[split_point:]
    return child1, child2

# Mutacja chromosomu przez dodanie lub usunięcie jednej godziny pracy
def mutate(chromosome):
    worker = random.randint(0, NUM_WORKERS - 1)
    if len(chromosome[worker]) == MIN_HOURS:
        chromosome[worker].append(random.choice(WORK_HOURS))
    elif len(chromosome[worker]) == NUM_HOURS:
        chromosome[worker].remove(random.choice(WORK_HOURS))
    else:
        if random.random() < 0.5:
            chromosome[worker].append(random.choice(WORK_HOURS))
        else:
            chromosome[worker].remove(random.choice(WORK_HOURS))
    return chromosome

def genetic_algorithm(population_size, generations):
    population = generate_population(population_size)
    for i in range(generations):
        population = sorted(population, key=evaluate_chromosome, reverse=True)
        print(f"Generation {i+1}, Best score: {evaluate_chromosome(population[0])}")
        if evaluate_chromosome(population[0]) == NUM_WORKERS:
            return population[0]
    selected = tournament_selection(population, population_size)
    offspring = []
    for i in range(0, population_size, 2):
        parent1 = population[i % len(population)]
        parent2 = population[(i+1) % len(population)]
        child1, child2 = crossover(parent1, parent2)
        offspring.append(mutate(child1))
        offspring.append(mutate(child2))
        population = offspring
    return population[0]

best_chromosome = genetic_algorithm(population_size=50, generations=100)
print(tabulate(best_chromosome, headers=[f"Worker {i+1}" for i in range(NUM_WORKERS)]))
