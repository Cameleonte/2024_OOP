from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    MORTGAGE_INTEREST_RATE = 0.035
    MORTGAGE_LOAN_AMOUNT = 50000.0

    def increase_interest_rate(self):
        self.STUDENTS_INTEREST_RATE * 0.005
