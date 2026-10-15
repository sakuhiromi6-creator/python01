class Plant:
    def __init__(self, nome: str, height: int, age: int):
        self.nome = nome
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.nome}: {self.height}cm, {self.age} days old")


print("=== Garden Plant Registry ====")

nome1 = Plant("Rose", 25, 30)
nome2 = Plant("Sunflower", 80, 45)
nome3 = Plant("Cactus", 15, 120)

nome1.show()
nome2.show()
nome3.show()
