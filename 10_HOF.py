'''
Asunto: Práctica de uso de funciones de orden superior aplicadas
a funciones lamba y funciones comunes
'''
# Declaramos la función increment
def increment(x):
    return x+1
# Pasamos como parámtero una función a la función higherOrderFunction
# para la práctica
def higherOrderFunction(x, func):
    return x+func(x)

# Esto produce que una función ejecute otra como si estuvieran
# anidadas
print(higherOrderFunction(1, increment))

# El mismo proceso puede realizarse mediante funciones lambda de orden
# superior
inc = lambda x : x+1
hof_lambda = lambda x,func : x+func(x)

print(hof_lambda(1,inc))