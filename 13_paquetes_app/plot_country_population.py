
'''
Asunto: Práctica que utiliza módulos de python para extraer datos de un archivo
csv y funciones para graficar de manera directa el crecimiento poblacional
de un país dentro del archivo csv
'''
# Importar módulos python
import read_csv
import charts

countries = read_csv.read_csv('./app/world_population.csv')

def extract_population(country):
    '''
    Función que extrae los elementos del país introducido en los parámetros buscándolo en
    el diccionario "countries", que contengan la palabra "Population" en su clave. 
    Por ejemplo si como entrada colocamos "Canada" buscar la información de este país en 
    el diccionario countries y extraer la población de todas las claves que contengan la palabra
    "Population" en su nombre para crear un nuevo diccionario de pura población por año
    '''
    population = {}
    country_info = list( filter(lambda countInfo : countInfo['Country/Territory'] == country, countries))
    country_keys = country_info[0].keys()
    for key in country_keys:
        if('Population' in key and 'World' not in key):
            key_name = key[:4]
            population[key_name] = float(country_info[0][key])
    return population

def extract_world_population():
    '''
    Función que extrae la columna entera de "World Population Percentage" del diccionario countries
    '''
    all_countries = list( map(lambda country : country['Country/Territory'], countries ))
    population = list( map(lambda country : float(country['World Population Percentage']), countries ))
    return all_countries, population

if __name__ == "__main__":
    
    # Búsqueda de población en Canada
    population = extract_population('Canada')
    # Almacenar en forma de lista valores y claves para graficarlos
    tags = list(population.keys())
    values = list(population.values())
    # Grafica de barras con la información invertida
    charts.generate_bar_chart(tags[::-1], values[::-1])
    
    
    # Extracción de población mundial
    all_countries, all_population = extract_world_population()
    # Grafica de barras con la información invertida
    charts.generate_pie_chart(all_population, all_countries)
