import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(
      csvfile, delimiter=','
    )  # el delimitador nos enseña cómo estan divididos nuestros datos, en este caso con una ',' pero podría ser con ';'
    header = next(
      reader)  # el reader es un iterable, es por esto que podemos usar "next"
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {
        key: value
        for key, value in iterable
      }  # de esta manera nos devolvería clave y valor correspondiente
      data.append(country_dict)  # aquí se agrega a la lista del data
    return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[8])
  population_list = [value for key, value in data() if 'Population' in key]
  print(population_list)
