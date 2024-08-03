from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    STUDENTS_INTEREST_RATE = 0.015
    STUDENTS_LOAN_AMOUNT = 2000.0

    def increase_interest_rate(self):
        self.STUDENTS_INTEREST_RATE * 0.002
