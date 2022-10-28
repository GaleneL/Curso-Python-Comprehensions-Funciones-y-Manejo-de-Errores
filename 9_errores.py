'''
Asunto: Práctica para el manejo de errores y excepciones en el
lenguaje de python
'''
# Uso de la estructura try catch para permitir el flujo de
# la aplicación aún si existen un error
print('flujo paso 1')
try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)
print('flujo paso 2')

# Función assert que asegura que el resultado de una operación
# sea cierto valor específico, de lo contrario da un error
# que interrumpe el flujo de ejecución del programa
suma = lambda x,y : x+y
assert suma(2,2) == 4
print('Hola2')

# Colocar una exception personalizada de acuerdo a una condición
# mediante raise
age = 10
if age < 18:
    raise Exception('No menores de edad')