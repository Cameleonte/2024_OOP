from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    MORTGAGE_INTEREST_RATE = 3.5
    MORTGAGE_LOAN_AMOUNT = 50000.0

    def __init__(self):
        super().__init__(self.MORTGAGE_INTEREST_RATE, self.MORTGAGE_LOAN_AMOUNT)

    def increase_interest_rate(self) -> None:
        self.interest_rate += 0.5
