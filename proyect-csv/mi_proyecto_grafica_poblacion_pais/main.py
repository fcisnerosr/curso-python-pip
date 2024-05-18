import os
from population_years import population_years
os.system('clear')

def run():
    # country = input('Write a country: ')
    country = 'Mexico'
    years, population = population_years(country)
    
if __name__ == '__main__':
    run()