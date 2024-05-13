from Chromosome import Chromosome
from Gene import Gene
from ClassicGenetic import ClassicGenetic
from Population import Population
import time

purchases = []
with open("D:\GIT\GeneticAlgorithms\data\chromosomes.txt", 'r') as file:
    for line in file:
        data = line.strip().split(',')
        purchase = Gene(int(data[0]), int(data[1]), data[2])
        purchases.append(purchase)

population = Population(10, 50000, 1, purchases)
population.fitness_all()
population.info()
# GeneticAlgorithm = ClassicGenetic(population, 0.1, 10)
# for i in range(0, 100):
#     GeneticAlgorithm.genetic_algorithm()
#     if i%10 == 0:
#         max = Chromosome(30)
#         max = GeneticAlgorithm.get_max_fitness()
#         print(str(max.fitness) + ' ' + str(max.get_time()))

