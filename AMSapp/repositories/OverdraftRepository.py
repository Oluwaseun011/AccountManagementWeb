from abc import ABCMeta, abstractmethod
from typing import List
from AMSapp.dto.OverdraftDto import *
from AMSapp.models import Overdraft

class OverdraftRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_overdraft(self, model:GetOverdraft):
        """Get Overdraft Object"""
        raise NotImplementedError

    # @abstractmethod
    # def list_overdraft_with_account_number(self, account_number: str) -> List[ListOverdrafts]:
    #     """List Overdraft Object"""
    #     raise NotImplementedError
    #
    # @abstractmethod
    # def overdraft_details_with_account_number(self, account_number: str) -> OverdraftDetails:
    #     """Overdraft Details Object"""
    #     raise NotImplementedError

class DjangoORMOverdraftOverdraft(OverdraftRepository):
    def get_overdraft(self, model: GetOverdraft):
        overdraft = Overdraft()
        overdraft.account_id = model.account_id
        overdraft.overdraft_amount = model.overdraft_amount
        overdraft.overdraft_balance = model.overdraft_balance
        overdraft.overdraft_status = model.overdraft_status
        overdraft.save()

    # def list_overdraft_with_account_number(self, account_number: str) -> List[ListOverdrafts]:
    #     overdraft = list(Overdraft.objects.values("account__account_pin", ""))