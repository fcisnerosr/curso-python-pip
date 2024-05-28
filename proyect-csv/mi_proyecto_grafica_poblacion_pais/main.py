import os; import matplotlib.pyplot as plt
from population_years import population_years
from graph import Graph
os.system('clear')

def run():
    # country = input('Write a country: ')
    country = 'Afghanistan'
    years, population = population_years(country)
    print(years)
    print(population)
    popu_graph = Graph(years, population)
    popu_graph.bar()
        
if __name__ == '__main__':
    run()
