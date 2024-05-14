from Chromosome import Chromosome

class Population:
    def __init__(self, population_size, max_budget, generate, data):
        self.populationSize = population_size
        self.chromosomeSize = len(data)
        self.maxBudget = max_budget
        self.chromosomes = []
        self.data = data

        if generate == 1:
            for i in range(population_size):
                chromosome = Chromosome(self.chromosomeSize, data)
                self.chromosomes.append(chromosome)

    def fitness_all(self):
        for chromosome in self.chromosomes:
            chromosome.calc_fitness(self.maxBudget)

    #TODO ереробити прінт
    def print(self):
        for i in range(self.populationSize):
            print("Chromosome %d" % i)
            self.chromosomes[i].print_chromosome()
            print()

    def print_fitness(self):
        for i in range(self.populationSize):
            # print("Chromosome %d" % i)
            # print("Fitness: %f" % self.chromosomes[i].fitness)
            print(self.chromosomes[i].get_fitness(), end=" ")

    def info(self):
        print("Population size: %d" % self.populationSize)
        print("Max budget: %d" % self.maxBudget)
        print("Chromosome size: %d" % self.chromosomeSize)
        for i in range(self.populationSize):
            print("Chromosome %d" % i)
            print(str(self.chromosomes[i].fitness))

    def calc_max_fitness(self):
        max_fitness = self.chromosomes[0].fitness
        temp = self.chromosomes[0]
        for chromosome in self.chromosomes:
            if chromosome.fitness > max_fitness:
                max_fitness = chromosome.fitness
                temp = chromosome
        return temp

    def get_best_chromosome(self, elitism):
        self.chromosomes.sort(key=lambda chromosome: chromosome.fitness, reverse=True)
        return self.chromosomes[:elitism]
