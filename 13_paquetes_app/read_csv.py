'''
Asunto: Módulo creado para manejar archivos CSV
'''
import csv

def read_csv(path):
    '''
    Función que abre un archivo con formato CSV y extrae los datos devolviendo
    una lista de diccionarios con cada columna del archivo
    '''
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        #print(header)
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key:value for key,value in iterable}
            data.append(country_dict)
        return data
             

if __name__ == '__main__':
    data = read_csv('./app/world_population.csv')
    print(data[35])