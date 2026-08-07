#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def record_grow(self) -> None:
            self.grow_calls += 1

        def record_age(self) -> None:
            self.age_calls += 1

        def record_show(self) -> None:
            self.show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow,"
                  f" {self.age_calls} age, {self.show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.age = 0
        self.height = 0.0
        self.stats = self._Stats()
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.age

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            self.age = 0
        else:
            self.age = new_age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            self.height = 0.0
        else:
            self.height = new_height

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self.stats.record_show()

    def grow(self) -> None:
        self.height += 2.1
        self.stats.record_grow()

    def grow_older(self) -> None:
        self.age += 1
        self.stats.record_age()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        self.color = color
        super().__init__(name, height, age)
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

        def record_shade(self) -> None:
            self.shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self.shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk: float) -> None:
        self.trunk = trunk
        super().__init__(name, height, age)
        self.stats: Tree._TreeStats = self._TreeStats()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk:.1f}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of"
              f" {self.get_height():.1f}cm long and {self.trunk:.1f}cm wide.")
        self.stats.record_shade()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 seed_count: int = 0) -> None:
        super().__init__(name, height, age, color)
        self.seed_count = seed_count

    def bloom(self) -> None:
        super().bloom()
        self.seed_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed_count}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()
    print()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.grow_older()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("=== Anonymous")
    mystery = Plant.create_anonymous()
    mystery.show()
    display_plant_stats(mystery)


if __name__ == "__main__":
    ft_garden_analytics()
