# Comentario agregado en GitHub
import pandas as pd
import utils
import read_csv
import charts
import os
os.system('clear')

def run():
  # data = read_csv.read_csv('data.csv')
  # data = list(filter(lambda item : item['Continent'] == 'South America',data))

  # countries = list(map(lambda x: x['Country'], data))
  # percentages = list(map(lambda x: x['World Population Percentage'], data))
  # charts.generate_pie_chart(countries, percentages)
  
  df          = pd.read_csv('data.csv')                   # lectura de csv con pandas as pd
  df          = df[df['Continent'] ==  'Africa']   # Redefinición de dt, busca todos los paises de 'South America'
  countries   = df['Country'].values                      # de la tabla dt, accede a los valores de la columna 'Country'
  
  percentages = df['World Population Percentage'].values
  
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  # print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()
  
