'''
Asunto: manejo de archivos mediante python con las funciones open,
readline, write y close así
'''
# Se abre un archivo mediante la función open y la ruta
file = open('./text.txt')
# readline funciona como un iterador, que lee cada línea del
# archivo una por una
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

# Método for que lee todas las lineas de una sola vez
for line in file:
    print(line)

# Siempre cerrar el archivo al terminar de usarlo
file.close()

# Para evitar cerrar un archivo, se puede usar la sintaxis
# with open(ruta, proceso) as file
with open('./text.txt', 'r+') as file: #no necesita el close o cerrarlo
    file.write('\nnuevas cosas en este archivo')
    for line in file:
        print(line)
#r+ permite leer y escribir todo normal
#w+ hace que se sobreescriba todo el archivo

