import re

f = open("data.txt", "r").read()

print(f)

data = re.findall(":.+", f)

number_of_iterations = data[0].replace(":", "").strip()
number_of_parents = data[1].replace(":", "").strip()
mutate_percent = data[2].replace(":", "").strip()
employees = data[3].replace(":", "").strip()
preferences = data[4].replace(":", "").strip()
antipreferences = data[5].replace(":", "").strip()

number_of_iterations = int(number_of_iterations)
number_of_parents = int(number_of_parents)
mutate_percent = int(mutate_percent)
employees = list(employees.split(","))
preferences = list(preferences.split(" "))
antipreferences = list(antipreferences.split(" "))

for i in range(len(preferences)):
    preferences[i] = list(preferences[i].replace("[", "").replace("]", "").split(","))
for i in range(len(antipreferences)):
    antipreferences[i] = list(antipreferences[i].replace("[", "").replace("]", "").split(","))

print(f'Number of iterations: {number_of_iterations}')
print(f'Number of parents: {number_of_parents}')
print(f'Mutate ratio: {mutate_percent}')
print(f'Employees: {employees}')
print(f'Preferences: {preferences}')
print(f'Antipreferences: {antipreferences}')