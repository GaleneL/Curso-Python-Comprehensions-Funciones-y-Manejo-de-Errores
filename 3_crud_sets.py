'''
Asunto: Práctica de operaciones de tipo CRUD con conjuntos
en el lenguaje de python
'''
# Declaración de un conjunto
set_countries = {'col','mex','bol'}

# Comprobación de tamaño y de existencia de elementos dentro del conjunto
size = len(set_countries)
print(size)
print('col' in set_countries)
print('pe' in set_countries)

# Añadir un elemento al conjunto
set_countries.add('pe')

# Función update para concatenar 2 conjuntos aunque no posean orden
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# Remover elementos de un conjunto
set_countries.remove('col')
print(set_countries)
#al remover algo que no existe dentro del conjunto, lanza un error
set_countries.remove('ar')
print(set_countries)

# Función discard quita elementos de un conjunto sin que haya errores si es que
# el elemento no existe
set_countries.discard('ar')
