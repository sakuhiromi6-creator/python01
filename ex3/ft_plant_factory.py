class Plant:
    def __init__(self, nome: str, height: float, days: int):
        self.nome = nome
        self.height = height
        self.days = days

    def show(self):
        print(
            f"Created: {self.nome}: {round(self.height, 1)}cm, "
            f"{self.days} days old"
        )


print("=== Plant Factory Output ===")
rose = Plant("Rose", 25.0, 30)
oak = Plant("Oak", 200.0, 365)
cactus = Plant("Cactus", 5.0, 90)
sunflower = Plant("Sunflower", 80.0, 45)
fern = Plant("Fern", 15.0, 120)

rose.show()
oak.show()
cactus.show()
sunflower.show()
fern.show()
