import random

# Ustawienie parametrów algorytmu
NUM_WORKERS = 2  # Liczba pracowników
NUM_HOURS = 8  # Liczba godzin pracy w ciągu dnia
MIN_HOURS = 2  # Minimalna liczba godzin pracy
WORK_HOURS = list(range(10, 20))  # Dostępne godziny pracy
TABU_DAY = 4  # Dzień tygodnia, który nie jest dostępny dla pracowników

# Ustawienie preferencji i wymagań pracowników
PREFERENCES = {
    0: [10, 11, 12, 13, 14],  # Preferowane godziny pracy dla pracownika 0
    1: [15, 16, 17, 18, 19],  # Preferowane godziny pracy dla pracownika 1
}
REQUIREMENTS = {
    0: [10, 11, 12, 13, 14],  # Wymagane godziny pracy dla pracownika 0
    1: [15, 16, 17, 18, 19],  # Wymagane godziny pracy dla pracownika 1
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
        chromosome[worker].remove(random.choice(chromosome[worker]))
    else:
        if random.random() < 0.5:
            chromosome[worker].append(random.choice(WORK_HOURS))
        else:
            chromosome[worker].remove(random.choice(chromosome[worker]))
    return chromosome

# Główna pętla algorytmu genetycznego
population_size = 50
generations = 100
mutation_rate = 0.1
population = generate_population(population_size)

for generation in range(generations):
    population = tournament_selection(population, population_size // 2)
    next_generation = []
    for i in range(population_size):
        parent1 = population[i % len(population)]
        parent2 = population[(i+1) % len(population)]
        child1, child2 = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            child1 = mutate(child1)
        if random.random() < mutation_rate:
            child2 = mutate(child2)
        next_generation.extend([child1, child2])

    population = next_generation + population[:population_size-len(next_generation)]

# Wyszukanie najlepszego rozwiązania
best_chromosome = max(population, key=evaluate_chromosome)
best_score = evaluate_chromosome(best_chromosome)
print("Najlepsze rozwiązanie: ")
for i in range(NUM_WORKERS):
    hours = best_chromosome[i]
    print("Pracownik {}: {}".format(i, hours))
print("Wartość funkcji celu: {}".format(best_score))
