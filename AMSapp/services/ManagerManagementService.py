from abc import abstractmethod, ABCMeta
from typing import List
from AMSapp.repositories.ManagerRepository import ManagerRepository
from AMSapp.dto.ManagerDto import *


class ManagerManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_manager(self, model: RegisterManager):
        """Register Manager Object"""
        raise NotImplementedError

    @abstractmethod
    def list_managers(self) -> List[ListManager]:
        """List Manager Objects"""
        raise NotImplementedError

    @abstractmethod
    def manager_details(self, manager_id: int) -> ManagerDetails:
        """Returns a Manager Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_manager(self, manager_id: int, model: EditManager):
        """Edit a Manager Object"""
        raise NotImplementedError




class DefaultManagerManagementService(ManagerManagementService):
    repository: ManagerRepository

    def __init__(self, repository: ManagerRepository):
        self.repository = repository

    def create_manager(self, model: RegisterManager):
        return self.repository.create_manager(model)

    def edit_manager(self, manager_id: int, model: EditManager):
        return self.repository.edit_manager(manager_id, model)

    def list_managers(self) -> List[ListManager]:
        return self.repository.list_managers()

    def manager_details(self, manager_id: int) -> ManagerDetails:
        return self.repository.manager_details(manager_id)