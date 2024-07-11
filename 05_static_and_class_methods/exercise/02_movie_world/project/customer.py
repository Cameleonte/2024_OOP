from project.dvd import DVD


class Customer:

    def __init__(self, name: str, age: int, id_: int):
        self.name = name
        self.age = age
        self.id = id_
        self.rented_dvds: list[DVD] = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's "
                f"({', '.join(dvd.name for dvd in self.rented_dvds)})")
