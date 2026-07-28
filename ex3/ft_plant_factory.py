#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm: {self.age} days old"
              )


def ft_garden_data() -> None:
    print("=== Plant Factory Output ===")
    print("Created:", end=' ')
    Plant("Rose", 25, 30).show()
    print("Created:", end=' ')
    Plant("Oak", 200, 365).show()
    print("Created:", end=' ')
    Plant("Cactus", 5, 90).show()
    print("Created:", end=' ')
    Plant("Sunflower", 80, 45).show()
    print("Created:", end=' ')
    Plant("Fern", 15, 120).show()


if __name__ == "__main__":
    ft_garden_data()
