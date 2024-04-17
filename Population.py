import Chromosome

class Population:
    def __init__(self, population_size, chromosome_size):
        self.populationSize = population_size
        self.chromosomeSize = chromosome_size
        self.chromosomes = []

        for i in range(population_size):
            self.chromosomes.append(Chromosome.Chromosome(chromosome_size))

    def fitness_all(self):
        for i in range(self.populationSize):
            self.chromosomes[i].calc_fitness()

    def print(self):
        for i in range(self.populationSize):
            print(self.chromosomes[i].chromosome + ' ' + str(self.chromosomes[i].fitness))
