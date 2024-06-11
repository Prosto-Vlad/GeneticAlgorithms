from Gene import Gene
from ClassicGenetic import ClassicGenetic
from ParallelGenetic import ParallelGenetic
from Population import Population
from Chromosome import Chromosome

purchases = []
with open("D:/Git/3 курс 2 семестр/GeneticAlgorithms/data/chromosomes.txt", 'r') as file:
    for line in file:
        data = line.strip().split(',')
        purchase = Gene(int(data[0]), int(data[1]), data[2])
        purchases.append(purchase)

population = Population(20, 15000, 1, purchases)
population.fitness_all()

ClassicAlgorithm = ClassicGenetic(population, 0.3, 0.8, 10)
ParallelGenetic = ParallelGenetic(population, 0.3, 0.8, 10)

i = 0
stop_iter = 0
max_fitness = 0
max_chrom = Chromosome(0,[])
while stop_iter < 10000:
    ParallelGenetic.genetic_algorithm()
    max_chrom = ParallelGenetic.get_max_fitness()
    if max_chrom.get_fitness() != max_fitness:
        max_fitness = max_chrom.get_fitness()
        stop_iter = 0
    else:
        stop_iter += 1
    i += 1
    if i%1 == 0:
        max_chrom = ParallelGenetic.get_max_fitness()
        print("Iter " + str(i))
        print("Max: " + str(max_chrom.get_fitness()))
        max_chrom.print_test()
        ParallelGenetic.population.print_fitness()
        print()

print("Result")
max_chrom = ParallelGenetic.get_max_fitness()
max_chrom.print_test()
ParallelGenetic.population.print_fitness()
max_chrom.print_test()

# i = 0
# stop_iter = 0
# max_fitness = 0
# max_chrom = Chromosome(0,[])
# while stop_iter < 10000:
#     ClassicAlgorithm.genetic_algorithm()
#     max_chrom = ClassicAlgorithm.get_max_fitness()
#     if max_chrom.get_fitness() != max_fitness:
#         max_fitness = max_chrom.get_fitness()
#         stop_iter = 0
#     else:
#         stop_iter += 1
#     i += 1
#     if i%1000 == 0:
#         max_chrom = ClassicAlgorithm.get_max_fitness()
#         print("Iter " + str(i))
#         print("Max: " + str(max_chrom.get_fitness()))
#         #max_chrom.print_test()
#         ClassicAlgorithm.population.print_fitness()
#         print()
#
# print("Result")
# max_chrom = ClassicAlgorithm.get_max_fitness()
# max_chrom.print_test()
# ClassicAlgorithm.population.print_fitness()
# max_chrom.print_test()