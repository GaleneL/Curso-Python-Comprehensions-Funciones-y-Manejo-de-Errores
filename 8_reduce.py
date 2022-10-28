'''
Asunto: Práctica del uso de la función reduce en el lenguaje
de python

Reduce toma una estructura de datos y la reduce a un solo término
como resulado el cual está determinado por la función que se le
coloque como entrada

Sintaxys: functools.reduce(lambda in, item : proceso, data)
'''
import functools

numbers = [1,2,3,4]
result = functools.reduce(lambda counter, item : counter+item, numbers)
print(result)