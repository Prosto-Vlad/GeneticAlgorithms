from Gene import Gene
from ClassicGenetic import ClassicGenetic
from Population import Population

purchases = []
with open("D:\GIT\GeneticAlgorithms\data\chromosomes.txt", 'r') as file:
    for line in file:
        data = line.strip().split(',')
        purchase = Gene(int(data[0]), int(data[1]), data[2])
        purchases.append(purchase)

population = Population(100, 10000, 1, purchases)
population.fitness_all()

GeneticAlgorithm = ClassicGenetic(population, 0.3, 5)
for i in range(0, 10000):
    GeneticAlgorithm.genetic_algorithm()
    if i%10 == 0:
        max_chrom = GeneticAlgorithm.get_max_fitness()
        print("Iter " + str(i))
        print("Max: " + str(max_chrom.get_fitness()))
        print()

max_chrom = GeneticAlgorithm.get_max_fitness()
max_chrom.print_test()
GeneticAlgorithm.population.print_fitness()