import re
def population_years(country):
    pattern1 = re.compile(r'^(\s\w{3},)([\w\s]*)')
    pattern2 = re.compile(r'\d{0,20}\.?\d{1,20}')

    # Years from head and find the population in the input country
    with open('./data.csv', 'r') as f:
        v_line = [line for line in f]

    with open('./data.csv', 'r') as f:
        for line in f:
            res = re.match(pattern1, line)
            if res:
                if res.group(2) == country:
                    population = re.findall(pattern2, line)
                    population = population[1:9]
                    population.sort()

    # Extract the head
    head = iter(v_line)
    head = next(head)

    # Find the years trough regex
    pattern = (r'\d{4,4}')
    years   = re.findall(pattern, head)
    years   = [int(year) for year in years]
    years.sort()
    years   = [str(year) for year in years]
    return years, population

if __name__ == '__main__':
    country = 'Afghanistan'
    years, population = population_years(country)
    print(years)
    print(population)