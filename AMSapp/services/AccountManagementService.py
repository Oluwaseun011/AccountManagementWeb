from abc import abstractmethod, ABCMeta
from AMSapp.dto.AccountDto import *
from AMSapp.models import Account
from typing import List
from AMSapp.repositories.AccountRepository import AccountRepository


class AccountManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_account(self, model: RegisterAccount):
        """Create Account Object"""
        raise NotImplementedError

    @abstractmethod
    def block_or_unblock_account(self, model: BlockAndUnblock):
        """Edit Account Object"""
        raise NotImplementedError

    @abstractmethod
    def deposit_or_withdrawal(self, model: DepositAndWithdraw):
        """Change Account Balance"""
        raise NotImplementedError

    @abstractmethod
    def transfer(self, model: Transfer):
        """Edit Objects"""
        raise NotImplementedError

    @abstractmethod
    def list_account(self) -> List[ListAccount]:
        """List Account Object"""
        raise NotImplementedError

    @abstractmethod
    def account_details(self, account_id) -> AccountDetails:
        """Account Details Object"""
        raise NotImplementedError

    @abstractmethod
    def get_account_with_account_holder(self, account_holder_id) -> AccountDetails:
        """Account Details Object"""
        raise NotImplementedError

    @abstractmethod
    def get_account_with_account_number(self, account_number: str) -> AccountDetails:
        """Account Details Object"""
        raise NotImplementedError


class DefaultAccountManagementService(AccountManagementService):
    repository: AccountRepository

    def __init__(self, repository: AccountRepository):
        self.repository = repository

    def create_account(self, model: RegisterAccount):
        return self.repository.create_account(model)

    def block_or_unblock_account(self, model: BlockAndUnblock):
        return self.repository.block_or_unblock_account(model)

    def deposit_or_withdrawal(self, model: DepositAndWithdraw):
        return self.repository.deposit_or_withdrawal(model)

    def list_account(self) -> List[ListAccount]:
        return self.repository.list_account()

    def account_details(self, account_id) -> AccountDetails:
        return self.repository.account_details(account_id)

    def get_account_with_account_holder(self, account_holder_id) -> AccountDetails:
        return self.repository.get_account_with_account_holder(account_holder_id)

    def transfer(self, model: Transfer):
        return self.repository.transfer(model)

    def get_account_with_account_number(self, account_number: str) -> AccountDetails:
        return self.repository.get_account_with_account_number(account_number)


