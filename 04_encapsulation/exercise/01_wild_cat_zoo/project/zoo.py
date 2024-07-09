from typing import List, Union
from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if price > self.__budget:
            return "Not enough budget"
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        curr_worker: Worker = next((w for w in self.workers if worker_name == w.name), None)
        if not curr_worker:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(curr_worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        sum_salaries = sum(w.salary for w in self.workers)
        if sum_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        money_for_animals = sum(a.money_for_care for a in self.animals)
        if money_for_animals > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= money_for_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        return self.__print_results(self.animals, "Lion", "Tiger", "Cheetah")

    def workers_status(self) -> str:
        return self.__print_results(self.workers, "Keeper", "Caretaker", "Vet")

    @staticmethod
    def __print_results(types: List[Union[Animal, Worker]], *args) -> str:
        zoo_animals_and_workers = {arg: [] for arg in args}
        for elem in types:
            zoo_animals_and_workers[elem.__class__.__name__].append(repr(elem))

        result = [f"You have {len(types)} {str(types[0].__class__.__bases__[0].__name__).lower()}s"]
        for key in args:
            value = zoo_animals_and_workers[key]
            result.append(f'----- {len(value)} {key}s:')
            result.extend(value)

        return '\n'.join(result)
