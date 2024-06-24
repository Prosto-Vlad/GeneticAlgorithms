from Gene import Gene
from ClassicGenetic import ClassicGenetic
from ParallelGenetic import ParallelGenetic
from Population import Population
from Chromosome import Chromosome
import time

if __name__ == '__main__':
    purchases = []
    with open("./data/chromosomes.txt", 'r') as file:
        for line in file:
            data = line.strip().split(',')
            purchase = Gene(int(data[0]), int(data[1]), data[2])
            purchases.append(purchase)

    chromosome_count = [100, 100, 500, 1000, 2500, 5000]
    process_cout = [2, 4, 6, 8, 10, 12]
    for i in range(len(chromosome_count)):
        print("---------------------------------")
        print(f"Chromosome count: {chromosome_count[i]}")
        print("---------------------------------")
        population = Population(chromosome_count[i], 10000, 1, purchases)
        population.fitness_all()

        # i = 0
        # stop_iter = 0
        # max_fitness = 0
        # timeList = []
        # while stop_iter < 20:
        #     classicAlgorithm = ClassicGenetic(population, 0.3, int(chromosome_count[i]*0.05))
        #
        #     start_time = time.time()
        #
        #     classicAlgorithm.genetic_algorithm()
        #
        #
        #     end_time = time.time()
        #
        #     total_time_in_seconds = end_time - start_time
        #     total_time_in_milliseconds = total_time_in_seconds * 1000
        #     timeList.append(total_time_in_milliseconds)
        #     stop_iter += 1
        #
        # print("Result")
        # max_chrom = classicAlgorithm.get_max_fitness()
        # max_chrom.print_test()
        # print()
        # mean_time = sum(timeList) / len(timeList)
        # print(f"Classic genetic algorithm executed in {mean_time:.2f} milliseconds")
        # for j in range(timeList.__len__()):
        #     print(f"Time {j+1}: {timeList[j]:.2f} milliseconds")
        #
        # print()

        for i in range(0, 20):
            i = 0
            stop_iter = 0
            max_fitness = 0
            timeList = []
            population_tpm = Population(chromosome_count[i], 10000, 1, purchases)
            population_tpm.fitness_all()
            while stop_iter < 10:
                population = population_tpm
                parallelGenetic = ParallelGenetic(population, 0.3, int(2500 * 0.05))

                start_time = time.time()

                parallelGenetic.genetic_algorithm(6)

                end_time = time.time()

                total_time_in_seconds = end_time - start_time
                total_time_in_milliseconds = total_time_in_seconds * 1000
                timeList.append(total_time_in_milliseconds)
                stop_iter += 1

        i = 0
        stop_iter = 0
        max_fitness = 0
        timeList = []
        population_tpm = Population(chromosome_count[i], 10000, 1, purchases)
        population_tpm.fitness_all()
        while stop_iter < 10:
            population = population_tpm
            parallelGenetic = ParallelGenetic(population, 0.3, int(chromosome_count[i]*0.05))

            start_time = time.time()

            parallelGenetic.genetic_algorithm(6)

            end_time = time.time()

            total_time_in_seconds = end_time - start_time
            total_time_in_milliseconds = total_time_in_seconds * 1000
            timeList.append(total_time_in_milliseconds)
            stop_iter += 1

        print("Result")
        max_chrom = parallelGenetic.get_max_fitness()
        max_chrom.print_test()
        print()
        mean_time = sum(timeList) / len(timeList)
        print(f"Parallel genetic algorithm executed in {mean_time:.2f} milliseconds")
        for j in range(timeList.__len__()):
            print(f"Time {j+1}: {timeList[j]:.2f} milliseconds")
            

