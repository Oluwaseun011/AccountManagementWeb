from django.http import HttpRequest
from django.shortcuts import redirect, render

from AMSapp.dto.AccountDto import DepositAndWithdraw
from AMSapp.models import Overdraft
from AMSapp.service_provider import ams_service_provider
from AMSapp.dto.OverdraftDto import *


def get_overdraft(request):
    context = {

    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("profile")
    return render(request, 'overdraft/get_overdraft.html', context)


def __get_overdraft_attribute_from_request(request: HttpRequest):
    get_overdraft_dto = GetOverdraft()
    get_overdraft_dto.account_number = request.POST['account_number']
    get_overdraft_dto.overdraft_amount = request.POST['amount']
    get_overdraft_dto.account_pin = request.POST['account_pin']
    return get_overdraft_dto


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            overdraft = __get_overdraft_attribute_from_request(request)
            account = ams_service_provider.account_management_service().get_account_with_account_number(
                account_number=overdraft.account_number)
            if account.account_pin == int(overdraft.account_pin):
                overdraft.overdraft_balance = overdraft.overdraft_amount
                overdraft.overdraft_status = 'active'
                __set_new_amount_for_overdraft(account.account_balance, account.account_number,
                                               overdraft.overdraft_amount)
                overdraft.account_id = account.id
                ams_service_provider.overdraft_management_service().get_overdraft(overdraft)
                context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e


def __set_new_amount_for_overdraft(account_balance: float, account_number: str, amount: float):
    transaction = DepositAndWithdraw()
    transaction.account_balance = __get_new_balance_on_overdraft(amount, account_balance)
    transaction.account_number = account_number
    ams_service_provider.account_management_service().deposit_or_withdrawal(transaction)

def __get_new_balance_on_overdraft(amount: float, account_balance):
    new_balance = account_balance - float(amount)
    return new_balance
