import os; import matplotlib.pyplot as plt
from population_years import population_years
from graph import Graph
os.system('clear')

def run():
    # country = input('Write a country: ')
    country = 'Mexico'
    years, population = population_years(country)
    popu_graph = Graph(years, population)
    popu_graph.bar()
        
if __name__ == '__main__':
    run()
