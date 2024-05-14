import numpy as np

class Chromosome:
    def __init__(self, size, data):
        self.genes = []
        self.size = size
        self.fitness = 0
        self.data = data

        self.genes = np.random.randint(2, size=self.size)

        self.total_popularity = 0
        self.total_cost = 0
        self.unique_genres = 0

    def get_fitness(self):
        return self.fitness

    def get_genes(self):
        return self.genes

    def get_size(self):
        return self.size

    def calc_fitness(self, max_budget):
        self.fitness = 0
        total_cost = 0
        total_count = 0
        total_popularity = 0
        genre_list = []

        for i in range(self.size):
            if self.genes[i] == 1:
                total_count += 1
                total_popularity += self.data[i].get_popularity()
                total_cost += self.data[i].get_cost()
                genre_list.append(self.data[i].get_genre())

        if total_cost > max_budget:
            self.fitness += (max_budget - total_cost) / 10

        self.fitness += total_popularity

        unique_genres = len(set(genre_list))
        self.fitness += unique_genres*10

        #test
        self.total_popularity = total_popularity
        self.total_cost = total_cost
        self.unique_genres = unique_genres
        #end test

        return self.fitness

    def print_chromosome(self):
        for i in range(self.size):
            print("Gene" + str(i) + ": " + str(self.data[i].get_popularity()) + " " + str(self.data[i].get_cost()) + " " + self.data[i].get_genre())

    def print_test(self):
        print("Fitness " + str(self.fitness))
        print("Popularity " + str(self.total_popularity))
        print("Cost " + str(self.total_cost))
        print("Genres " + str(self.unique_genres))
        for i in range(self.size):
            if self.genes[i] == 1:
                print("Gene" + str(i) + ": " + str(self.data[i].get_popularity()) + " " + str(self.data[i].get_cost()) + " " + self.data[i].get_genre())
        print()