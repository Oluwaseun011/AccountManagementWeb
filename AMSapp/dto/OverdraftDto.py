class GetOverdraft:
    account_id: int
    account_number: str
    account_pin: int
    overdraft_amount: float
    overdraft_balance: float
    overdraft_status: str


class ListOverdrafts:
    loan_id: int
    account_id: int
    account_number: str
    overdraft_amount: float
    overdraft_balance: float
    overdraft_status: str


class OverdraftDetails:
    loan_id: int
    account_id: int
    account_number: str
    overdraft_amount: float
    overdraft_balance: float
    overdraft_status: str
