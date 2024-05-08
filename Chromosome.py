import random
from Gene import Gene

class Chromosome:
    def __init__(self, size):
        self.genes = []
        self.size = size
        self.fitness = 0

    def generate(self, data):
        time = 0
        while time <= self.size:
            gene = data.pop(random.randint(0, len(data) - 1))
            self.genes.append(gene)
            time += gene.time
        if time > self.size:
            self.genes.pop()

    def calc_fitness(self):
        for gene in self.genes:
            gene.calc_fitness()

    def print_chromosome(self):
        for gene in self.genes:
            gene.print_chromosome()
