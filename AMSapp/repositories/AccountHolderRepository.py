from abc import abstractmethod, ABCMeta
from typing import List

from django.contrib.auth.models import User, Group

from AMSapp.models import AccountHolder, Account
from AMSapp.dto.AccountHolderDto import *


class AccountHolderRepository(metaclass=ABCMeta):
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


class DjangoORMAccountHolderRepository(AccountHolderRepository):
    def create_account_holder(self, model: RegisterAccountHolder) -> int:
        account_holder = AccountHolder()
        # create a user object
        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

        # adds the user object to the account holder instance
        account_holder.user = user
        group = Group.objects.get(name="AccountHolder")
        user.groups.add(group)

        account_holder.address = model.address
        account_holder.phone_number = model.phone_number
        account_holder.sex = model.sex
        account_holder.date_of_birth = model.date_of_birth
        account_holder.save()
        account_holder_id = account_holder.id
        return account_holder_id

    def edit_account_holder(self, account_holder_id: int, model: EditAccountHolder):
        try:
            account_holder = AccountHolder.objects.get(id=account_holder_id)
            account_holder.user.username = model.username
            account_holder.user.first_name = model.first_name
            account_holder.user.last_name = model.last_name
            account_holder.user.email = model.email
            account_holder.user.save()
            account_holder.phone_number = model.phone_number
            account_holder.address = model.address
            account_holder.sex = model.sex
            account_holder.date_of_birth = model.date_of_birth
            account_holder.save()
        except AccountHolder.DoesNotExist as e:
            raise e

    def list_account_holders(self) -> List[ListAccountHolder]:
        account_holders = list(
            AccountHolder.objects.values('id', 'user__username', 'user__first_name', 'user__last_name',
                                         'phone_number'))
        results: List[ListAccountHolder] = []

        for account_holder in account_holders:
            item = ListAccountHolder()
            item.id = account_holder['id']
            item.phone_number = account_holder['phone_number']
            item.first_name = account_holder['user__first_name']
            item.last_name = account_holder['user__last_name']
            item.username = account_holder['user__username']
            results.append(item)
        return results

    def account_holder_details(self, account_holder_id: int) -> AccountHolderDetails:
        try:
            account_holder = AccountHolder.objects.get(id=account_holder_id)
            item = AccountHolderDetails()
            try:
                account = Account.objects.get(account_holder_id=item.id)

                item.id = account_holder.id
                item.phone_number = account_holder.phone_number
                item.first_name = account_holder.user.first_name
                item.last_name = account_holder.user.last_name
                item.username = account_holder.user.username
                item.email = account_holder.user.email
                item.date_of_birth = account_holder.date_of_birth
                item.address = account_holder.address
                item.sex = account_holder.sex
                item.balance = account.account_balance
                item.status = account.account_status
                return item
            except Account.DoesNotExist as e:
                raise e
        except AccountHolder.DoesNotExist as e:
            raise e

    def get_details_by_user(self, user_id: int) -> AccountHolderDetails:
        account_holder = AccountHolder.objects.values("user__first_name", 'user__last_name', 'user__username',
                                                      'account__account_status', 'account__account_number',
                                                      'account__account_balance', 'id').get(user_id=user_id)
        item = AccountHolderDetails()
        item.id = account_holder['id']
        item.phone_number = account_holder['user__first_name']
        item.first_name = account_holder['user__first_name']
        item.last_name = account_holder['user__last_name']
        item.username = account_holder['user__username']
        item.account_status = account_holder['account__account_status']
        item.account_balance = account_holder['account__account_balance']
        item.account_number = account_holder['account__account_number']
        return item
