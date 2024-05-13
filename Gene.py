

class Gene:
    def __init__(self, cost, popularity, genre):
        self.cost = cost
        self.genre = genre
        self.popularity = popularity

    def print_gene(self):
        print(self.popularity + ', ' + str(self.cost))

    def get_popularity(self):
        return self.popularity

    def get_genre(self):
        return self.genre

    def get_cost(self):
        return self.cost
