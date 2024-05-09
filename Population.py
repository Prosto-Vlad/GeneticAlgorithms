from Chromosome import Chromosome


class Population:
    def __init__(self, population_size, chromosome_size, generate, data):
        self.populationSize = population_size
        self.chromosomeSize = chromosome_size
        self.chromosomes = []
        #TODO можливо переробити генерацію. Зробити так, аби воно максимально заповняло
        if generate == 1:
            for i in range(population_size):
                temp = Chromosome(self.chromosomeSize)
                temp.generate(data)
                self.chromosomes.append(temp)

    def fitness_all(self):
        for i in range(self.populationSize):
            self.chromosomes[i].calc_fitness()

    # def best_fitness(self):
    #     for i in range(self.populationSize):
    #         if self.chromosomes[i].calc_fitness() == 1:
    #             return self.chromosomes[i]

    def print(self):
        for i in range(self.populationSize):
            print("Chromosome %d" % i)
            self.chromosomes[i].print_chromosome()


    #TODO переробити вибір найкращої хромосоми, якщо потрібно
    # def best_chromosome(self, elitism):
    #     self.chromosomes.sort(key=lambda chromosome: chromosome.fitness, reverse=True)
    #     return self.chromosomes[:elitism]
