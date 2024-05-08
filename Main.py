from Chromosome import Chromosome
from Gene import Gene
from ClassicGenetic import ClassicGenetic
from Population import Population
import time

# initPopulation = Population(population_size=100, chromosome_size=10000, generate=1)
#
# initPopulation.fitness_all()
#
# geneticAlgorithm = ClassicGenetic(initPopulation, 0.02, 4)
#
# end = 0
# start_time = time.time()
#
# while end != 1:
#     pop = geneticAlgorithm.genetic_algorithm()
#     print("------------------------")
#     print(pop.chromosomes[0].fitness)
#     if pop.fitness_all() == 1:
#         pop.best_fitness().print_chromosome()
#         end = 1
#
# end_time = time.time()
#
# elapsed_time_microseconds = (end_time - start_time) * 1e6
#
# print("Час виконання: {:.2f} мікросекунд".format(elapsed_time_microseconds))

purchases = []
with open("D:\GIT\GeneticAlgorithms\data\chromosomes.txt", 'r') as file:
    for line in file:
        data = line.strip().split(',')
        purchase = Gene(data[0], float(data[1]), float(data[2]), int(data[3]))
        purchases.append(purchase)

chromosome = Chromosome(10)
chromosome.generate(purchases)
chromosome.print_chromosome()