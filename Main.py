from ClassicGenetic import ClassicGenetic
from Population import Population

initPopulation = Population(population_size=20, chromosome_size=5)

initPopulation.fitness_all()

geneticAlgorithm = ClassicGenetic(initPopulation, 0.02, 4)

geneticAlgorithm.print()


