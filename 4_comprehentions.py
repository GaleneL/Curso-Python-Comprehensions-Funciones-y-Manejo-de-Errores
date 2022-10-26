'''
Asunto: Práctica para explorar list comprehentions y 
dictionary comprehentions y su funcionalidad

Sintaxys: 
var_name = [ element for element <iterable> if <condition> ]
var_name = { key:value for element1, element2 <iterable> if <condition> }
'''
import random

# Lists Comprehentions .....................
# Ejemplo de ejecución común
numbers = []
for element in range(1,11):
    numbers.append(element*2)
print(numbers)
# Ejemplo de ejecución con una list comprehention
numbers2 = [element2*2 for element2 in range(1,11)]
print(numbers2)
# Ejemplo de ejecución con una list complehention más una condición
numbers3 = [element3*2 for element3 in range(1,11) if element3 % 2 == 0]
print(numbers3)

# Dictionary Complehention .....................
# Ejemplo de ejecución común
dict = {}
for i in range(1,11):
    dict[i] = i*2
print(dict)
# Ejemplo de ejecución con una dictionary comprehention
dict2 = {i:i*2 for i in range(1,11)}
print(dict)

# Crear un diccionario de países añadiendo un valor de población
# aleatorio

# Ejecución normal
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)
print(population)
# Ejecución con dictionary comprehentions
population2 = {country:random.randint(1,100) for country in countries}
print(population2)

# Creando un diccionario a partir de dos listas
names = ['nico', 'zule', 'santi']
ages = [12,56,98]

dictPeople = {names[i]:ages[i] for i in range(len(names))}
print(dictPeople)

# Creando un diccionario a partir de dos listas con una condición
dictPeople2 = {name:age for (name,age) in zip(names,ages) if age>50 }
print(dictPeople2)