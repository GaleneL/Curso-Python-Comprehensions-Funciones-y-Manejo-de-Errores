'''
Asunto: Práctica del uso de la función filter en el lenguaje de python
para extraer información de estructuras de datos mediante un condicional
o un filtro lambda

Filter extrae elementos de una estructura de datos siempre y cuando
cumplan con la condición a la cual están siendo evaluados por la
función que se le pase como parámetro

Sintaxys: filter(lambda value : condition, data)
'''
# Extraer los números pares de la lista numbers mediante filer
numbers = [1,2,3,4,5]
new_numbers = list( filter(lambda x : x%2 == 0, numbers) )
print(new_numbers)

# Crear una lista de diccionarios con los elementos cuya clave "home_team_result" sea igual a 
# "Win", filtrando esa condición mediante filter
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)
print(len(matches))

winners = list( filter(lambda match : match['home_team_result'] == 'Win', matches) )

print(winners)
print(len(winners))
