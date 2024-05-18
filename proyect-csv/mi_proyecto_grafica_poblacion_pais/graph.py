import matplotlib.pyplot as plt

class Graph():
    def __init__(self, years, population):
        self.years = years
        self.population = population
        
    def bar(years, population):
        pass
        # fig, ax = plt.subplots()
        ## Pendiente de hacer objetos bar
        

    def pie(years, population):
        fig, ax = plt.subplots()
        ax.pie(years, population = population)
        plt.grid()
        plt.show()