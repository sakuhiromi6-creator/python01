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


print("=== Garden Plant Growth ===")

nome = Plant("Rose", 25.0, 30)
nome.show()
initial_height = nome.height

for giorno_1 in range(1, 8):
    print(f"=== Day {giorno_1} ===")
    nome.age()
    nome.grow()
    nome.show()

final_height = nome.height
growth = final_height - initial_height
print(f"Growth this week: {round(growth, 1)}cm")
