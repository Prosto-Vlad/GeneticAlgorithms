from ClassicGenetic import ClassicGenetic
from Population import Population

initPopulation = Population(population_size=20, chromosome_size=20, generate=1)

initPopulation.fitness_all()

geneticAlgorithm = ClassicGenetic(initPopulation, 0.02, 4)

end = 0

while end != 1:
    pop = geneticAlgorithm.genetic_algorithm()
    print("------------------------------------------------------------------------")
    pop.print()
    if pop.fitness_all() == 1:
        pop.best_fitness().print_chromosome()
        end = 1
