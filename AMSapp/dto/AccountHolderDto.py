from datetime import date


class RegisterAccountHolder:
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    account_pin: int
    address: str
    phone_number: str
    sex: str
    date_of_birth: date


class EditAccountHolder:
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    address: str
    phone_number: str
    sex: str
    date_of_birth: date
    date_updated: date


class ListAccountHolder:
    id: int
    username: str
    first_name: str
    last_name: str
    phone_number: str


class AccountHolderDetails:
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    address: str
    phone_number: str
    date_of_birth: date
    sex: int
    account_balance: float
    account_status: str
    account_number: str
