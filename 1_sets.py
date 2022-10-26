'''
Asunto: Práctica para el aprendizaje de conjuntos dentro del lenguaje
de python

Características de conjuntos: No se repiten los elementos, son mutables,
no poseen orden
'''
# Distintos conjuntos de varios tipos de datos
set_countries = {'col','mex','bol'}
set_numbers = {1,2,2,3,5,2}
set_types = {1,2,2,'hola',False,12.2}

# Transformar un string en un conjunto
set_from_string = set('hooola')

# Transformar una tupla en un conjunto
set_from_tuple = set(('abc','cbc','as','abc'))

# Transformar una lista en un conjunto
list = [1,1,5,7,9,4]
set_from_list = set(list)

# visualizar datos
print(set_from_list)
print(type(set_types))

