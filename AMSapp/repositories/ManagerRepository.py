from abc import abstractmethod, ABCMeta
from typing import List

from django.contrib.auth.models import User, Group

from AMSapp.models import Manager
from AMSapp.dto.ManagerDto import *


class ManagerRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_manager(self, model: RegisterManager):
        """Register Account Holder Object"""
        raise NotImplementedError

    @abstractmethod
    def list_managers(self) -> List[ListManager]:
        """List account Holder Objects"""
        raise NotImplementedError

    @abstractmethod
    def manager_details(self, account_holder_id: int) -> ManagerDetails:
        """Returns an Account Holder Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_manager(self, account_holder_id: int, model: EditManager):
        """Edit an Account Holder Object"""
        raise NotImplementedError


class DjangoORMManagerRepository(ManagerRepository):
    def create_manager(self, model: RegisterManager):
        manager = Manager()
        # create a user object
        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

        # adds the user object to the account holder instance
        manager.user = user
        group = Group.objects.get_or_create(name="Manager")
        user.groups.add(group)

        manager.address = model.address
        manager.phone_number = model.phone_number
        manager.date_of_birth = model.date_of_birth
        manager.save()

    def edit_manager(self, account_holder_id: int, model: EditManager):
        try:
            manager = Manager.objects.get(id=account_holder_id)
            manager.user.username = model.username
            manager.user.first_name = model.first_name
            manager.user.last_name = model.last_name
            manager.user.email = model.email
            manager.user.save()
            manager.phone_number = model.phone_number
            manager.address = model.address
            manager.date_of_birth = model.date_of_birth
            manager.save()
        except Manager.DoesNotExist as e:
            raise e

    def list_managers(self) -> List[ListManager]:
        managers = list(
            Manager.objects.values('id', 'user__username', 'user__first_name', 'user__last_name',
                                         'phone_number'))
        results: List[Manager] = []

        for account_holder in managers:
            item = ListManager()
            item.id = account_holder['id']
            item.phone_number = account_holder['phone_number']
            item.first_name = account_holder['user__first_name']
            item.last_name = account_holder['user__last_name']
            item.username = account_holder['user__username']
            results.append(item)
        return results

    def manager_details(self, account_holder_id: int) -> ManagerDetails:
        try:
            manager = Manager.objects.get(id=account_holder_id)
            item = ManagerDetails()
            item.id = manager.id
            item.phone_number = manager.phone_number
            item.first_name = manager.user.first_name
            item.last_name = manager.user.last_name
            item.username = manager.user.username
            item.email = manager.user.email
            item.date_of_birth = manager.date_of_birth
            item.address = manager.address
            return item
        except Manager.DoesNotExist as e:
            raise e
