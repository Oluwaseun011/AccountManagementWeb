from abc import ABCMeta, abstractmethod
from typing import List
from AMSapp.dto.OverdraftDto import *
from AMSapp.models import Overdraft
from AMSapp.repositories.OverdraftRepository import OverdraftRepository

class OverdraftManagementService(metaclass=ABCMeta):
    @abstractmethod
    def get_overdraft(self, model:GetOverdraft):
        """Get Overdraft Object"""
        raise NotImplementedError

class DefaultOverdraftManagementService(OverdraftManagementService):
    repository: OverdraftRepository

    def __init__(self, repository: OverdraftRepository):
        self.repository = repository

    def get_overdraft(self, model:GetOverdraft):
        return self.repository.get_overdraft(model)
