#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_height(self) -> float:
        return self.height

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Height can not be negative")
            print("Height update rejected")
            return
        self.height = value
        print(f"Height updated: {value:.1f}cm")

    def get_age(self) -> int:
        return self.age

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Age can not be negative")
            print("Age update rejected")
            return
        self.age = value
        print(f"Age updated: {value} days")

    def show(self) -> None:
        print(
            f"{self.name}: {self.height:.1f}cm, {self.age} "
            f"days old")


if __name__ == "__main__":
    print(" === Garden Security System ===")
    plant = Plant("Rose", 15, 10)
    print(
        f"Plant created: {plant.name}: {plant.get_height():.1f}cm, "
        f"{plant.get_age()} days old")

    plant.set_height(30)
    plant.set_age(15)
    print()

    plant.set_height(-5)
    plant.set_age(-10)
    print()

    print("Current state: ", end=" ")
    plant.show()
