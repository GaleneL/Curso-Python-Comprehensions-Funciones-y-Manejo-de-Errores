'''
Asunto: Observar el comportamiento de módulos externos dentro de un
script de python realizando ejemplos con los módulos
sys
re
time
collections
'''
# Módulo que permite acceder a información del sistema como la ruta
# en la que se encuentra este archivo
import sys
print(sys.path)

# Expresiones que tienen su propia sintxis, en este caso la función
# findall se utiliza aquí para encontrar dentro del texto y extraer
# todos los números que se encuentren en él
import re
text = 'Mi número de telefono es 311 123 121, el código del pais es 57, mi número de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)

# Módulo para obtener información sobre el tiempo, fechas, horas, entre otros
import time
timestamp = time.time()
local = time.localtime()
local = time.asctime(local)
print(timestamp)
print(local)

# Módulo para realizar operaciones entre estructuras de datos
# en este caso se cuenta la cantidad de veces que se repite un valor
# en la lista numbers devolviendo un diccionario con estos
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)