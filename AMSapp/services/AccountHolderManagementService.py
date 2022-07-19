from abc import abstractmethod, ABCMeta
from typing import List
from AMSapp.repositories.AccountHolderRepository import AccountHolderRepository
from AMSapp.dto.AccountHolderDto import *


class AccountHolderManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_account_holder(self, model: RegisterAccountHolder) -> int:
        """Register Account Holder Object"""
        raise NotImplementedError

    @abstractmethod
    def list_account_holders(self) -> List[ListAccountHolder]:
        """List account Holder Objects"""
        raise NotImplementedError

    @abstractmethod
    def account_holder_details(self, account_holder_id: int) -> AccountHolderDetails:
        """Returns an Account Holder Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_account_holder(self, account_holder_id: int, model: EditAccountHolder):
        """Edit an Account Holder Object"""
        raise NotImplementedError

    @abstractmethod
    def get_details_by_user(self, user_id: int) -> AccountHolderDetails:
        """Return Account Holder Object"""
        raise NotImplementedError



class DefaultAccountHolderManagementService(AccountHolderManagementService):
    repository: AccountHolderRepository

    def __init__(self, repository: AccountHolderRepository):
        self.repository = repository

    def create_account_holder(self, model: RegisterAccountHolder) -> int:
        return self.repository.create_account_holder(model)

    def edit_account_holder(self, account_holder_id: int, model: EditAccountHolder):
        return self.repository.edit_account_holder(account_holder_id, model)

    def list_account_holders(self) -> List[ListAccountHolder]:
        return self.repository.list_account_holders()

    def account_holder_details(self, account_holder_id: int) -> AccountHolderDetails:
        return self.repository.account_holder_details(account_holder_id)

    def get_details_by_user(self, user_id: int) -> AccountHolderDetails:
        return self.repository.get_details_by_user(user_id)
