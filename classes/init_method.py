# self parameter - basic implementation

class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

nairobi = City("Nairobi", "Kenya", 4397073, ["Nairobi National Park", "Karen Blixen Museum", "Giraffe Centre"])

new_york = City("New York", "USA", 8175133, ["Statue of Liberty", "Empire State Building", "Central Park"])

print(vars(nairobi))
print(vars(new_york))