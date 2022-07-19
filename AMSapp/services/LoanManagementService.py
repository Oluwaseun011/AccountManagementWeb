from abc import ABCMeta, abstractmethod
from typing import List
from AMSapp.dto.LoanDto import *
from AMSapp.models import Loan
from AMSapp.repositories.LoanRepository import LoanRepository


class LoanManagementServices(metaclass=ABCMeta):
    @abstractmethod
    def get_loan(self, model: GetLoan):
        """Get Loan Object"""
        raise NotImplementedError

    @abstractmethod
    def list_loan(self) -> List[ListLoan]:
        """List Loan Objects"""
        raise NotImplementedError

    @abstractmethod
    def loan_details(self, loan_id: int) -> LoanDetails:
        """Loan Details Object"""
        raise NotImplementedError

    @abstractmethod
    def loan_details_by_account_number(self, account_number: str) -> LoanDetails:
        """Loan Details Object"""
        raise NotImplementedError

    @abstractmethod
    def pay_loan(self, model: PayLoan):
        """Pay Loan"""
        raise NotImplementedError

    @abstractmethod
    def list_loan_by_account_number(self, account_number: str) -> List[ListLoan]:
        """Loan Details Object"""
        raise NotImplementedError


class DefaultLoanManagementServices(LoanManagementServices):
    repository: LoanRepository

    def __init__(self, repository: LoanRepository):
        self.repository = repository

    def get_loan(self, model: GetLoan):
        return self.repository.get_loan(model)

    def list_loan(self) -> List[ListLoan]:
        return self.repository.list_loan()

    def loan_details(self, loan_id: int) -> LoanDetails:
        return self.repository.loan_details(loan_id)

    def loan_details_by_account_number(self, account_number: str) -> LoanDetails:
        return self.repository.loan_details_by_account_number(account_number)

    def pay_loan(self, model: PayLoan):
        return self.repository.pay_loan(model)

    def list_loan_by_account_number(self, account_number: str) -> List[ListLoan]:
        return self.repository.list_loan_by_account_number(account_number)
