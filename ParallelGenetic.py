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

    def wheel_selection(self, population):
        total_fitness = sum(abs(chromosome.fitness) for chromosome in population)
        for _ in range(len(population)):
            rand = random.uniform(0, total_fitness)
            current_sum = 0
            for chromosome in population:
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
    def offspring_task(population):
        self, population = population.copy()

        result = []

        for i in range(len(population)):
            parent1 = self.wheel_selection(population)
            parent2 = self.wheel_selection(population)

            child = self.crossover(parent1, parent2)
            child = self.mutate(child)

            child.calc_fitness(self.population.maxBudget)

            result.append(child)

        return result

    def genetic_algorithm(self, process_count):
        temp_population = []
        temp_population[:self.elitism] = self.population.get_best_chromosome(self.elitism)
        population_for_task = self.population.chromosomes[self.elitism:]

        chunk_size = round(len(population_for_task)/process_count)
        chunks = []
        for i in range(0, len(population_for_task), chunk_size):
            temp = [self, ]
            if i + chunk_size > len(population_for_task):
                temp.append(population_for_task[i:])
            else:
                temp.append(population_for_task[i:i + chunk_size])
            chunks.append(temp)

        with multiprocessing.Pool(process_count) as pool:
            offsprings = pool.map(ParallelGenetic.offspring_task, chunks)

        for group in offsprings:
            for item in group:
                temp_population.append(item)

        result = Population(self.population.populationSize, self.population.maxBudget, 0, self.population.data)
        result.chromosomes = temp_population

        self.population = result


        return result