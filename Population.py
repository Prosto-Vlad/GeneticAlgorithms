from Chromosome import Chromosome


class Population:
    def __init__(self, population_size, generate, file_path):
        self.populationSize = population_size
        self.chromosomes = []
        #TODO доробити генерацію
        #if generate == 1:


    def fitness_all(self):
        for i in range(self.populationSize):
            self.chromosomes[i].calc_fitness()

    # def best_fitness(self):
    #     for i in range(self.populationSize):
    #         if self.chromosomes[i].calc_fitness() == 1:
    #             return self.chromosomes[i]

    def print(self):
        for i in range(self.populationSize):
            self.chromosomes[i].print_chromosome()
    #TODO переробити вибір найкращої хромосоми, якщо потрібно
    # def best_chromosome(self, elitism):
    #     self.chromosomes.sort(key=lambda chromosome: chromosome.fitness, reverse=True)
    #     return self.chromosomes[:elitism]
