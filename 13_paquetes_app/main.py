import mod

data = [{
		'Country': 'Colombia',
		'Population': 500
	},
	{
		'Country': 'Bolivia',
		'Population': 300
	}
	]

def run():
	keys, vals = mod.get_population()
	print(keys, vals)

	result = mod.population_by_country(data,'Colombia')
	print(result)

if __name__ == '__main__': #solo si se ejecuta como script en la terminal, pero si se ejecuta como módulo ignora esto
	run()