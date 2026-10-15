class Plant:
    def __init__(self, nome: str, height: float, age: int):
        self._nome = nome
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self._height

    def set_height(self, new_height):
        if new_height < 0:
            print(
                f"{self._nome}: "
                f"Error, height can't be negative \nHeight update rejected"
            )
        else:
            self._height = new_height

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age < 0:
            print(
                f"{self._nome}: "
                f"Error, age can't be negative \nAge update rejected"
            )
        else:
            self._age = new_age

    def __str__(self):
        return f"{self._nome}: {self._height}cm, {self._age} days old"


print("=== Garden Security System ===")

rose = Plant("Rose", 15.0, 10)
print(f"Plant created: {rose}\n")

new_height = 25.0
rose.set_height(new_height)
print(f"Height updated: {new_height}cm")

new_age = 30
rose.set_age(new_age)
print(f"Age updated: {new_age} days\n")

error_height = -5
rose.set_height(error_height)
error_age = -3
rose.set_age(error_age)

print(f"\nCurrent state: {rose}")
