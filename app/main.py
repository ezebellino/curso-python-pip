import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('data.csv')
  #De la siguiente manera podemos filtrarlos de manera tal que queden sólo países de sudamérica
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)


  country = input('Type country please => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country) 
    charts.generate_bar_chart(country["Country/Territory"], labels, values)

# con este if se logra que el archivo actual (main.py) pueda correr su función sin necesidad de tener que ser llamada por example.py .

if __name__ == '__main__':
  run()
