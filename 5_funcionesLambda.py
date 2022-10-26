'''
Asunto: Práctica de comparación de funciones normales con
funciones lambda en el lenguaje de python

Sintaxis: var_name = lambda entrada : salida
'''
# Ejemplo de una función común que incrementa el valor de entrada 
def increment(x):
    return x+1
result = increment(10)
print(result)

# Ejemplo de una función lambda que incrementa el valor de entrada 
increment2 = lambda x : x+1
result2 = increment2(20)
print(result2)

# Ejemplo de función lambda con varios parámetros de entrada
full_name = lambda name, last_name : f'Full name is {name.title()} {last_name.title()}'
print(full_name('Eduard','Stark'))