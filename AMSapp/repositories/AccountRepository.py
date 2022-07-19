from abc import ABCMeta, abstractmethod
from typing import List
from AMSapp.dto.AccountDto import *
from AMSapp.models import Account, AccountHolder


class AccountRepository(metaclass=ABCMeta):
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



class DjangoORMAccountRepository(AccountRepository):
    def create_account(self, model: RegisterAccount):
        account = Account()
        account.account_holder_id = model.account_holder_id
        account.account_number = model.account_number
        account.account_pin = model.account_pin
        account.account_balance = model.account_balance
        account.account_status = model.account_status
        account.save()

    def block_or_unblock_account(self, model: BlockAndUnblock):
        account = Account.objects.get(account_number=model.account_number)
        account.account_status = model.account_status
        account.save()

    def deposit_or_withdrawal(self, model: DepositAndWithdraw):
        account = Account.objects.get(account_number=model.account_number)
        account.account_balance = model.account_balance
        account.save()

    def transfer(self, model: Transfer):
        account = Account.objects.get(account_number=model.account_number)
        destination = Account.objects.get(account_number=model.recipient_number)
        account.account_balance = model.account_balance
        destination.account_balance = model.recipient_balance
        account.save()
        destination.save()

    def list_account(self) -> List[ListAccount]:
        accounts = list(Account.objects.values('id', 'account_number', 'account_status'))
        results: List[ListAccount] = []

        for account in accounts:
            item = ListAccount()
            item.account_number = account.account_number
            item.account_status = account.account_status
            results.append(item)
        return results

    def account_details(self, account_id) -> AccountDetails:
        account = Account.objects.get(id=account_id)
        item = AccountDetails()
        item.id = account.id
        item.account_number = account.account_number
        item.account_pin = account.account_pin
        item.account_status = account.account_status
        item.account_balance = account.account_balance
        item.date_created = account.date_created
        return item

    def get_account_with_account_holder(self, account_holder_id) -> AccountDetails:
        account = Account.objects.get(account_holder_id=account_holder_id)
        item = AccountDetails()
        item.id = account.id
        item.account_number = account.account_number
        item.account_pin = account.account_pin
        item.account_status = account.account_status
        item.account_balance = account.account_balance
        item.date_created = account.date_created
        return item

    def get_account_with_account_number(self, account_number: str) -> AccountDetails:
        account = Account.objects.get(account_number=account_number)
        item = AccountDetails()
        item.id = account.id
        item.account_number = account.account_number
        item.account_pin = account.account_pin
        item.account_status = account.account_status
        item.account_balance = account.account_balance
        item.date_created = account.date_created
        return item






