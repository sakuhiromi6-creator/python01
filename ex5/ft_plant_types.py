class Plant:
    def __init__(self, nome: str, height: float, days: int):
        self.nome = nome
        self.height = height
        self.days = days

    def show(self):
        print(
            f"{self.nome}: {round(self.height, 1)}cm, {self.days} days old"
        )

    def grow(self):
        self.height += 0.8

    def age(self):
        self.days += 1


class Flower(Plant):
    def __init__(self, nome: str, height: float, days: int, color: str):
        super().__init__(nome, height, days)
        self.color = color

    def bloom(self):
        print(f"{self.nome} is blooming beautifully!")

    def show(self):
        super().show()
        print(f"Color: {self.color}")


class Tree(Plant):
    def __init__(self, nome: str, height: float, days: int, diameter: float):
        super().__init__(nome, height, days)
        self.diameter = diameter

    def produce_shade(self):
        print(
            f"Tree {self.nome} now produces a shade of {self.height}cm long "
            f"and {self.diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, nome: str,
        height: float,
        days: int,
        harvest_season: str
    ):
        super().__init__(nome, height, days)
        self.harvest_season = harvest_season
        self.nutr_value = 0

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutr_value}")

    def grow(self):
        self.height += 2.1

    def age(self):
        super().age()
        self.nutr_value += 1


print("=== Garden Plant Types ===")
print("=== Flower")
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
print("Rose has not bloomed yet")
print("[asking the rose to bloom]")
rose.show()
rose.bloom()
print()
print("=== Tree")
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()
print("[asking the oak to produce shade]")
oak.produce_shade()
print()
print("=== Vegetable")
tomato = Vegetable("Tomato", 5.0, 10, "April")
tomato.show()
print("[make tomato grow and age for 20 days]")

for _ in range(20):
    tomato.grow()
    tomato.age()

tomato.show()
