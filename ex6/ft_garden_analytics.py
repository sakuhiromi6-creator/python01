class Plant():
    class Stato():
        def __init__(self):
            self.__growup = 0
            self.__ageup = 0
            self.__showup = 0

        def setgrow(self):
            self.__growup += 1

        def setage(self):
            self.__ageup += 1

        def setshow(self):
            self.__showup += 1

        def returnvalue(self):
            return (
                f"Stats: {self.__growup} grow, "
                f"{self.__ageup} age, "
                f"{self.__showup} show"
            )

    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days
        self.stats = self.Stato()

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")
        self.stats.setshow()

    def grow(self, change):
        self.height += change
        self.stats.setgrow()

    def age(self, diff):
        self.days += diff
        self.stats.setage()

    @staticmethod
    def is_older_than_a_year(days):
        return days > 365

    @classmethod
    def unknown(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, days: int, color: str, seeds: int
    ):
        super().__init__(name, height, days, color)
        self.seeds = seeds

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    class statstree(Plant.Stato):
        def __init__(self):
            super().__init__()
            self.__produce_shade = 0

        def setshade(self):
            self.__produce_shade += 1

        def returnvalue(self):
            return (super().returnvalue() +
                    "\n" + f"{self.__produce_shade} shade")

    def __init__(self, name: str, height: float, days: int, diameter: float):
        super().__init__(name, height, days)
        self.diameter = diameter
        self.stats = self.statstree()

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.diameter}cm")

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of {self.height}cm long "
            f"and {self.diameter}cm wide."
        )
        self.stats.setshade()


print("=== Garden statistics ===")
print("=== Check year-old")
print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")
print()
print("=== Flower")
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
print("[statistics for Rose]")
print(rose.stats.returnvalue())
print("[asking the rose to grow and bloom]")
rose.grow(8)
rose.bloom()
rose.show()
print("[statistics for Rose]")
print(rose.stats.returnvalue())
print()
print("=== Tree")
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()
print("[statistics for Oak]")
print(oak.stats.returnvalue())
print("[asking the oak to produce shade]")
oak.produce_shade()
print("[statistics for Oak]")
print(oak.stats.returnvalue())
print()
print("=== Seed")
sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
sunflower.show()
print("[make sunflower grow, age and bloom]")
sunflower.grow(30)
sunflower.age(20)
sunflower.bloom()
sunflower.seeds = 42
sunflower.show()
print("[statistics for Sunflower]")
print(sunflower.stats.returnvalue())
print()
print("=== Anonymous")
anonymous = Plant.unknown()
anonymous.show()
print("[statistics for Unknown plant]")
print(anonymous.stats.returnvalue())
