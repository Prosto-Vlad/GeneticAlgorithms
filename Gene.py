

class Gene:
    def __init__(self, name, cost, worth, time):
        self.cost = cost
        self.worth = worth
        self.time = time
        self.name = name
        self.fitness = 0


    def calc_fitness(self):
        self.fitness = 0
        self.fitness = self.fitness + (1/self.cost)*10
        self.fitness = self.fitness + self.worth

    def print_chromosome(self):
        print('| ' + self.name + ' | ' + str(self.cost) + ' | ' + str(self.worth) + ' | ' + str(self.time) + ' |')