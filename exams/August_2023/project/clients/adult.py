from project.clients.base_client import BaseClient


class Adult(BaseClient):
    ADULT_INITIAL_INTEREST = 4

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.ADULT_INITIAL_INTEREST)

    def get_new_interest(self):
        new_adult_interest = self.ADULT_INITIAL_INTEREST + self.ADULT_INITIAL_INTEREST * 0.2
        return new_adult_interest
