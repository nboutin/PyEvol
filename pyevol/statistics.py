

class Statistics:

    def __init__(self):
        self.maximums = [0]

    def update(self, creatures):
        foods = [c.food for c in creatures]

        self.maximums.append(max(foods))
        # print(self.maximums)
