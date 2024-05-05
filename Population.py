import Chromosome


class Population:
    def __init__(self, population_size, chromosome_size, generate):
        self.populationSize = population_size
        self.chromosomeSize = chromosome_size
        self.chromosomes = []

        if generate == 1:
            for i in range(population_size):
                self.chromosomes.append(Chromosome.Chromosome(chromosome_size))

    def fitness_all(self):
        for i in range(self.populationSize):
            self.chromosomes[i].calc_fitness()
            if self.chromosomes[i].fitness == self.chromosomeSize:
                return 1

    def best_fitness(self):
        for i in range(self.populationSize):
            if self.chromosomes[i].calc_fitness() == 1:
                return self.chromosomes[i]

    def print(self):
        for i in range(self.populationSize):
            print(self.chromosomes[i].chromosome + ' ' + str(self.chromosomes[i].fitness))

    def best_chromosome(self, elitism):
        self.chromosomes.sort(key=lambda chromosome: chromosome.fitness, reverse=True)
        return self.chromosomes[:elitism]
