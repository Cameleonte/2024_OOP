from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    STUDENTS_INTEREST_RATE = 1.5
    STUDENTS_LOAN_AMOUNT = 2000.0

    def __init__(self):
        super().__init__(self.STUDENTS_INTEREST_RATE, self.STUDENTS_LOAN_AMOUNT)

    def increase_interest_rate(self) -> float:
        return self.STUDENTS_INTEREST_RATE * 0.2
