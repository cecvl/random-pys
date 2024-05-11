class Pokemon:
    def __init__(self, entry , name ,types , level , region, height , weight ,description , is_caught ):
        self.entry = entry
        self.name = name
        self.types = types
        self.level = level
        self.region = region
        self.height = height
        self.weight = weight
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(f"{self.name} {self.name}!")
    def dispaly_details(self):
        print(f"Entry: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Types: {self.types}")
        print(f"Level: {self.level}")
        print(f"Region: {self.region}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")
        print(f"Description: {self.description}")
        if self.is_caught == True:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet.")          

pikapika = Pokemon(25, "Pikachu", "Electric", 50, "Kanto", 0.4, 6.0, "This intelligent Pokémon roasts hard berries with electricity to make them tender enough to eat.", False)
pikapika.speak()
pikapika.dispaly_details()   