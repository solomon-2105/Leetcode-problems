class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.Rated = {}
        self.mp = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.Rated:
                self.Rated[cuisine] = SortedSet(key=lambda x: (x[0], x[1]))
            self.Rated[cuisine].add((-rating, food))
            self.mp[food] = (rating, cuisine)

    def changeRating(self, food, newRating):
        rating, cuisine = self.mp[food]
        self.Rated[cuisine].discard((-rating, food))
        self.Rated[cuisine].add((-newRating, food))
        self.mp[food] = (newRating, cuisine)

    def highestRated(self, cuisine):
        return self.Rated[cuisine][0][1]