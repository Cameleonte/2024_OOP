from project.clients.base_client import BaseClient


class Student(BaseClient):
    STUDENT_INITIAL_INTEREST = 2

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.STUDENT_INITIAL_INTEREST)

    def get_new_interest(self):
        new_student_interest = self.STUDENT_INITIAL_INTEREST + 1
        return new_student_interest
