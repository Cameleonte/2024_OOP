from abc import abstractmethod


class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return "Meowwww"


class Dog(Animal):

    def make_sound(self):
        return "Bau-bau"


class Chicken(Animal):

    def make_sound(self):
        return "pi, pi, pi"


def animal_sound(animals: list[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat('Micia'), Dog('Baro'), Chicken('Pipi')]
animal_sound(animals)
