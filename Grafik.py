import pandas as pd
import random
from Converter import *

chromosome = [['A','B','C'],['D','E','F']]

def mutate(chromosome):
    if mutate_percent <= random.randint(1,100):
        mutated_gene = random.randint(0, 1)
        mutation = random.choice(chromosome[mutated_gene])
        i = chromosome[mutated_gene].index(mutation)
        chromosome[mutated_gene][i] = random.choice(employees)

mutate(chromosome)
print(chromosome)