from datetime import date


class GetLoan:
    account_id: int
    account_pin: int
    account_number: str
    loan_balance: float
    loan_status: str
    loan_type: str
    loan_amount: float
    date_created: date
    date_updated = date


class ListLoan:
    loan_balance: float
    loan_status: str
    loan_type: str
    loan_amount: float
    date_created: date
    date_updated: date
    account_pin: int
    loan_id: int


class LoanDetails:
    id: int
    account_number: str
    account_balance: float
    loan_balance: float
    loan_status: str
    loan_type: str
    loan_amount: float
    date_created: date
    date_updated = date


class PayLoan:
    loan_id: int
    loan_balance: float
    loan_status: str
    loan_type: str
    loan_amount: float
    amount: float
    account_number: str
    account_pin: int
    date_created: date
    date_updated = date
