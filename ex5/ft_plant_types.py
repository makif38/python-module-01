#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.age = 0
        self.height = 0.0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            self.age = 0
            print(f"Age Rejected {new_age}: Enter Valid Age")
        else:
            self.age = new_age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            self.height = 0.0
            print(
                f"{new_height} Rejected: Height can't"
                "be zero or negative"
                            )
        else:
            self.height = new_height

    def show(self) -> None:
        print(f"{self.name}: {round(self.get_height()):.1f}cm,"
              f" {self.get_age()} days old"
              )

    def grow(self) -> None:
        self.height += 2.1

    def grow_older(self) -> None:
        self.age = self.age + 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        self.color = color
        super().__init__(name, height, age)
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color : {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk: float) -> None:
        self.trunk = trunk
        super().__init__(name, height, age)

    def show(self) -> None:
        super().show()
        print(f"Trunk Diameter: {self.trunk:.1f}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of"
              f" {self.get_height():.1f}cm long and {self.trunk:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest: str,
                 _value: float) -> None:
        self.harvest = harvest
        self._value = _value
        super().__init__(name, height, age)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest}")
        print(f"Nutritional value: {self._value}")

    def grow(self) -> None:
        super().grow()
        self._value += 1


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flowers = Flower("Rose", 15, 10, "red")
    flowers.show()
    print("[asking the rose to bloom]")
    flowers.bloom()
    flowers.show()

    print("=== Tree")
    trees = Tree("Oak", 200, 365, 5)
    trees.show()
    print("[asking the oak to produce shade]")
    trees.produce_shade()

    print("=== Vegetable")
    vegetables = Vegetable("Tomato", 5, 10, "April", 0)
    vegetables.show()
    vegetables.set_age(10)
    print(f"[make {vegetables.name} grow and age for 20"
          f" days]")
    for _ in range(20):
        vegetables.grow()
        vegetables.grow_older()
    vegetables.show()


if __name__ == "__main__":
    ft_plant_types()
