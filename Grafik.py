#Algorytm do zarządzania pracą w firmie,
#tworzący grafik dla n pracowników w tygodniu
import random
from tabulate import tabulate

print("podaj pracowników po spacji")
pracownik = input()

podaniPracownicy = pracownik.split(" ")

terminy = [10,12,14,16,18,20]
pon = []
wt = []
sr = []
czw = []
pt = []
sob = []

for termin in terminy:
    pon.append(random.choice(podaniPracownicy))

for termin in terminy:
    wt.append(random.choice(podaniPracownicy))

for termin in terminy:
    sr.append(random.choice(podaniPracownicy))

for termin in terminy:
    czw.append(random.choice(podaniPracownicy))

for termin in terminy:
    pt.append(random.choice(podaniPracownicy))

for termin in terminy:
    sob.append(random.choice(podaniPracownicy))

wynik = [terminy, pon, wt, sr, czw, pt, sob]

wynik[0].insert(0,"  ")
wynik[1].insert(0,"pon")
wynik[2].insert(0,"wt")
wynik[3].insert(0,"sr")
wynik[4].insert(0,"czw")
wynik[5].insert(0,"pt")
wynik[6].insert(0,"sob")
print(tabulate(wynik, tablefmt="fancy_grid"))


def evaluate(a,b):
    print("hoho")

