import copy
import random

from Chromosome import Chromosome


class ClassicGenetic:
    def __init__(self, population, mutation_rate, elitism):
        self.population = population
        self.mutationRate = mutation_rate
        self.elitism = elitism

    def print(self):
        self.population.print()

    def wheel_selection(self):
        self.population.fitness_all()
        total_fitness = sum(chromosome.fitness for chromosome in self.population.chromosomes)
        for _ in range(len(self.population.chromosomes)):
            rand = random.uniform(0, total_fitness)  # Генеруємо випадкове число
            current_sum = 0
            for chromosome in self.population.chromosomes:
                current_sum += chromosome.fitness
                if current_sum >= rand:
                    return chromosome

    def crossover(self, parent1, parent2):
        temp1 = ""
        crossover_point = int(len(parent1.chromosomes))
        temp = parent1.chromosomes[0:crossover_point]
        temp.extend(parent2.chromosomes[crossover_point:])

        child = Chromosome(self.population.chromosomeSize)
        child.chromosome = temp1
        child.calc_fitness()
        return child

    def mutate(self, chromosome):
        if random.random() < self.mutationRate:
            mutation_point = random.randint(0, len(chromosome.chromosome) - 1)
            geneslist = list(chromosome.chromosome)
            geneslist[mutation_point] = "0" if geneslist[mutation_point] == "1" else "1"
            chromosome.chromosome = ''.join(geneslist)
            chromosome.calc_fitness()
            return chromosome

    def genetic_algorithm(self):
        # Доробити алгоритм
        return
