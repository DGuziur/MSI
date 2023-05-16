import pandas as pd

# df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
#                   index=['row 1', 'row 2'],
#                   columns=['col 1', 'col 2'])
# df1.to_excel("output.xlsx")

# C:\Users\Dawid\Downloads\MSI.xlsx

def evaluate_fitness(chromosome):
    fitness = 0
    for i in range(len(chromosome)-1):
      if chromosome[i] == chromosome[i + 1]:
        fitness +=1
    if chromosome[0] != 1:
        fitness += 1
    if chromosome[2] != 2:
        fitness += 1
    return fitness


df1 = pd.DataFrame(columns=["iteracja", "osobnik","fitness"])
osobnik = [5, 7, 8, 8, 9, 10]
for i in range(4):
    df2 = pd.DataFrame([[i, osobnik, evaluate_fitness(osobnik)]],
                   index=[i],
                   columns=["iteracja", "osobnik","fitness"])
    df1 = pd.concat([df1, df2])

df1.to_excel("Wynik.xlsx")