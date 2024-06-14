import random
import multiprocessing
from Chromosome import Chromosome
from Population import Population

class ParallelGenetic:
    def __init__(self, population, mutation_rate, elitism):
        self.population = population
        self.mutationRate = mutation_rate
        self.elitism = elitism

    def print(self):
        self.population.print()

    def get_max_fitness(self):
        return self.population.calc_max_fitness()

    def wheel_selection(self):
        total_fitness = sum(abs(chromosome.fitness) for chromosome in self.population.chromosomes)
        for _ in range(len(self.population.chromosomes)):
            rand = random.uniform(0, total_fitness)
            current_sum = 0
            for chromosome in self.population.chromosomes:
                current_sum += abs(chromosome.fitness)
                if current_sum >= rand:
                    return chromosome

    def crossover(self, parent1, parent2):
        child = Chromosome(self.population.chromosomeSize, self.population.data)
        temp = []

        for i in range(parent1.get_size()):
            rand = random.randint(0, abs(int(parent1.get_fitness() + parent2.get_fitness())))
            if rand <= parent1.get_fitness():
                temp.append(parent1.get_genes()[i])
            else:
                temp.append(parent2.get_genes()[i])

        child.chromosomes = temp

        return child

    def mutate(self, chromosome):
        if random.random() < self.mutationRate:
            for i in range(3):
                mutation_point = random.randint(0, len(chromosome.genes) - 1)
                chromosome.genes[mutation_point] = "0" if chromosome.genes[mutation_point] == "1" else "1"
            return chromosome
        else:
            return chromosome
    
    @staticmethod
    def offspring_task(args):
        self, population_data = args
        parent1 = self.wheel_selection()
        parent2 = self.wheel_selection()

        child = self.crossover(parent1, parent2)
        child = self.mutate(child)

        return child

    def genetic_algorithm(self, process_count):
        temp_population = []
        temp_population[:self.elitism] = self.population.get_best_chromosome(self.elitism)

        pool_args = [(self, 0,)]

        with multiprocessing.Pool(process_count) as pool:
            offsprings = pool.map(ParallelGenetic.offspring_task, pool_args)

        temp_population[self.elitism:] = offsprings

        result = Population(self.population.populationSize, self.population.maxBudget, 0, self.population.data)
        result.chromosomes = temp_population

        self.population = result
        self.population.fitness_all()

        return result