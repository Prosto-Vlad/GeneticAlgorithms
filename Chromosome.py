import math
import random
from Gene import Gene
import numpy as np

class Chromosome:
    def __init__(self, size):
        self.genes = []
        self.size = size
        self.fitness = 0

        self.genes = np.random.randint(2, size=self.size)

    def calc_fitness(self, data, maxBudget):
        total_cost = 0
        total_count = 0
        total_popularity = 0
        genre_list = []

        for i in range(self.size):
            if self.genes[i] == 1:
                total_count += 1
                total_popularity += data[i].get_popularity()
                total_cost += data[i].get_cost()/100
                genre_list.append(data[i].get_genre())

        self.fitness += (total_cost/total_count)
        self.fitness += total_popularity

        

        if total_cost > maxBudget:
            self.fitness += maxBudget - total_cost

        return self.fitness

    def print_chromosome(self):
        for gene in self.genes:
            gene.print_gene()
