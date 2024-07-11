from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity() -> int:
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if self.CUSTOMER_CAPACITY > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if self.DVD_CAPACITY > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        curr_dvd = next((dvd for dvd in self.dvds if dvd_id == dvd.id), None)
        curr_client = next((client for client in self.customers if customer_id == client.id), None)
        if curr_dvd in curr_client.rented_dvds:
            return f"{curr_client.name} has already rented {curr_dvd.name}"
        if curr_dvd.is_rented:
            return "DVD is already rented"
        if curr_client.age < curr_dvd.age_restriction:
            return f"{curr_client.name} should be at least {curr_dvd.age_restriction} to rent this movie"

        curr_dvd.is_rented = True
        curr_client.rented_dvds.append(curr_dvd)
        return f"{curr_client.name} has successfully rented {curr_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        curr_client = next((client for client in self.customers if customer_id == customer_id), None)
        curr_dvd = next((dvd for dvd in curr_client.rented_dvds if dvd_id == dvd.id), None)
        if curr_dvd:
            curr_dvd.is_rented = False
            curr_client.rented_dvds.remove(curr_dvd)
            return f"{curr_client.name} has successfully returned {curr_dvd.name}"
        return f"{curr_client.name} does not have that DVD"

    def __repr__(self):
        result = '\n'.join([c.__repr__() for c in self.customers]) + '\n'
        result += '\n'.join([d.__repr__() for d in self.dvds])
        return result
