from datetime import date


class RegisterAccount:
    account_holder_id: int
    account_number: str
    account_pin: int
    account_balance: float
    account_status: str


class BlockAndUnblock:
    account_number: str
    account_status: str
    date_updated: date


class DepositAndWithdraw:
    account_number: str
    account_balance: str
    account_pin: int
    amount: float
    date_updated: date

class Transfer:
    account_number: str
    account_balance: float
    recipient_number: str
    recipient_balance: float
    account_pin: int
    amount: float
    date_updated: date


class ListAccount:
    id: int
    account_number: str
    account_status: str
    date_created: date


class AccountDetails:
    id: int
    account_number: str
    account_pin: int
    account_balance: float
    account_status: str
    date_created: date
