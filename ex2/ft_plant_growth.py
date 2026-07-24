#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.day1_height = height

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self):
        self.height = self.height + 0.8

    def grow_older(self):
        self.age = self.age + 1


def ft_garden_data():
    print("=== Garden Plant Growth ===")
    plant = Plant("Rose", 25.0, 30)
    for i in range(1, 8):
        print("=== Day " + str(i) + " ===")
        plant.show()
        plant.grow()
        plant.grow_older()
    print(
        f"Growth this week: {round((plant.height - plant.day1_height), 2)} cm")


if __name__ == "__main__":
    ft_garden_data()
