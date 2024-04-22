import random

class Chromosome:
    def __init__(self, chromosome_size):
        self.chromosomeSize = chromosome_size
        self.chromosome = ''.join([random.choice(['0', '1']) for _ in range(self.chromosomeSize)])
        self.fitness = 0

    def calc_fitness(self):
        self.fitness = 0
        for i in range(self.chromosomeSize):
            if self.chromosome[i] == '1':
                self.fitness += 1
        if self.fitness == self.chromosomeSize:
            return 1
        else:
            return 0

    def print_chromosome(self):
        print(self.chromosome)
