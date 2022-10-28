'''
Asunto: Práctica de función map para transformar variables de entrada
a través de funciones

Map aplica una función a cada uno de los elementos de una estructura
de datos, es decir transforma cada elemento de la estructura

Sintaxis: var_name = map(function , var_entrada)

'''
# Transformación de la lista numbers con una función común
numbers = [1,2,3,4]
numbers2 = []
for i in numbers:
    numbers2.append(i*2)
print(numbers)
print(numbers2)

# Transformación de la lista numbers con función map y función lambda
numbers3 = map(lambda i : i*2, numbers)
print(list(numbers3))

# Transformación de dos listas de entrada en un solo resultado
numbers4 = [5,6,7]
result = list( map(lambda x,y : x+y, numbers,numbers4) )
print(result)

# Extrayendo una lista de datos desde un diccionario con la función map .................
# Diccionario
items = [
    {
        'producto' : 'camisa',
        'precio' : 100
    },
    {
        'producto' : 'pantalones',
        'precio' : 300
    },
    {
        'producto' : 'falda',
        'precio' : 200
    },
]

# Crear una lista que extraiga los datos de precios del diccionario anterior
precios = list( map(lambda producto : producto['precio'], items) )
print(precios)

# Añadir valores al diccionario anterior
# Función que calcula el IVA y lo añade a un diccionario de entrada
def add_iva(items):
    new_item = items.copy() # Función copy para evitar que el diccionario origianl sea manipulado por ser un apuntador
    new_item['taxes'] = new_item['precio']*0.16
    return new_item

itemsIVA = list( map(add_iva, items) )
print(items)
print(itemsIVA)
