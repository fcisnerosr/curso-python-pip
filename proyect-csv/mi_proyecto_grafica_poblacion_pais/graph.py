import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Graph():
    def __init__(self, years, population):
        self.years = years
        self.population = population
        
    def bar(self):
        fig, ax = plt.subplots()
        ax.bar(self.years, self.population)
        plt.grid()
        plt.show()
        
    def pie(self, country):
        
        fig, ax = plt.subplots()
        ax.pie(self.years, labels = self.population)
        plt.grid()
        plt.show()
        
