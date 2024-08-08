from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_CLIENT_TYPES = {
        "Student": Student,
        "Adult": Adult
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str) -> str:
        if not self.VALID_LOAN_TYPES.get(loan_type):
            raise Exception("Invalid loan type!")
        current_loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(current_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if self.VALID_CLIENT_TYPES.get(client_type) is None:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        current_client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(current_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self._get_client(client_id)
        if ((client.__class__.__name__ == "Student" and loan_type == "MortgageLoan") and
                (client.__class__.__name__ == "Adult" and loan_type == "StudentLoan")):
            raise Exception("Inappropriate loan type!")

        for count, loan_to_move in enumerate(self.loans):
            if loan_to_move.__class__.__name__ == loan_type:
                first_loan_of_type = self.loans.pop(count)
                client.loans.append(first_loan_of_type)
                break

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self._get_client(client_id)
        self.clients.remove(client)
        if client.loans:
            return "The client has loans! Removal is impossible!"
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0
        for curr_loan in self.loans:
            if curr_loan.__class__.__name__ == loan_type:
                number_of_changed_loans += 1
                BaseLoan.increase_interest_rate(curr_loan)
        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        number_client_interests_changed = 0
        lst_with_clients_min_interest = [cl for cl in self.clients if cl.interest < min_rate]
        for curr_client in lst_with_clients_min_interest:
            number_client_interests_changed += 1
            curr_client.increase_clients_interest()
        return f"Number of clients affected: {number_client_interests_changed}."

    def get_statistics(self):
        total_clients_income = sum(client.income for client in self.clients)

        loans_count_granted_to_clients = sum([len(client.loans) for client in self.clients if client.loans])
        granted_sum = sum([loan.amount for c in self.clients for loan in c.loans])

        loans_count_not_granted = len(self.loans)
        tot_sum_not_granted_loans = sum(loan.amount for loan in self.loans)

        sum_rates = sum([client.interest for client in self.clients])
        try:
            avg_client_interest_rate = sum_rates / len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0

        return f"Active Clients: {len(self.clients)}\n" \
               f"Total Income: {total_clients_income:.2f}\n" \
               f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" \
               f"Available Loans: {loans_count_not_granted}, Total Sum: {tot_sum_not_granted_loans:.2f}\n" \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

    def _get_client(self, client_id):
        try:
            client = [c for c in self.clients if c.client_id == client_id][0]
            return client
        except IndexError:
            raise Exception("No such client!")
