'''
Asunto: Práctica de operaciones con conjuntos en el
lenguaje de python
'''
# Declaración de 2 conjuntos
set_a = {'col','mex','bol'}
set_b = {'pe', 'bol'}

# Union entre conjuntos
set_union = set_a.union(set_b)
print(set_union)
print(set_a | set_b)

# Intersección entre conjuntos
set_inter = set_a.intersection(set_b)
print(set_inter)
print(set_a & set_b)

# Diferencia de conjuntos
set_dif = set_a.difference(set_b)
print(set_dif)
print(set_a - set_b)

# Diferencia simétrica de conjuntos
set_symetricDiff = set_a.symmetric_difference(set_b)
print(set_symetricDiff)
print(set_a ^ set_b)