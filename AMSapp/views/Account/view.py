from django.contrib.auth.decorators import login_required

from AMSapp.service_provider import ams_service_provider
from django.shortcuts import redirect, render
from django.http import HttpRequest
from AMSapp.dto.AccountDto import *
import random
from datetime import date
from AMSapp.models import Account


def create_account_if_post_method(request, account_holder_id: int, context):
    if request.method == 'POST':
        try:
            account = __get_attribute_from_request(request)
            account.account_holder_id = account_holder_id
            account.account_number = __get_account_number()
            account.account_balance = 0.0
            account.account_status = 'active'
            account.date_created = date.today()
            ams_service_provider.account_management_service().create_account(account)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e


def __get_attribute_from_request(request: HttpRequest):
    register_account_dto = RegisterAccount()
    register_account_dto.account_pin = request.POST['pin']
    return register_account_dto


def __get_account_number():
    tag = 'CODE'
    number = str(random.randint(10000, 99999))
    account_number = tag + number
    return account_number


@login_required
def withdrawal(request):
    context = {

    }
    __withdraw_if_post(request, context)
    if request.method == 'POST' and context['message']:
        return redirect('profile')
    return render(request, 'account/withdraw.html', context)


@login_required
def deposit(request):
    context = {

    }
    __deposit_if_post(request, context)
    if request.method == 'POST' and context['message']:
        return redirect('profile')
    return render(request, 'account/deposit.html', context)


@login_required
def transfer(request):
    context = {

    }
    __transfer_if_post(request, context)
    if request.method == 'POST' and context['message']:
        return redirect('profile')
    return render(request, 'account/transfer.html', context)


def __get_transfer_attribute_by_request(request: HttpRequest):
    transfer_dto = Transfer()
    transfer_dto.account_number = request.POST["account_number"]
    transfer_dto.account_pin = request.POST["account_pin"]
    transfer_dto.recipient_number = request.POST["recipient_number"]
    transfer_dto.amount = request.POST["amount"]
    return transfer_dto


def __transfer_if_post(request, context):
    if request.method == 'POST':
        try:
            transaction = __get_transfer_attribute_by_request(request)
            account_holder = ams_service_provider.account_holder_management_service().get_details_by_user(
                request.user.id)
            account = ams_service_provider.account_management_service().get_account_with_account_holder(
                account_holder.id)
            recipient = ams_service_provider.account_management_service().get_account_with_account_number(
                transaction.recipient_number)
            if account.account_pin == int(transaction.account_pin):
                new_balance = __get_new_balance(balance=account.account_balance, amount=transaction.amount,
                                                action='transfer')
                recipient_new_balance = __get_recipient_new_balance(balance=recipient.account_balance,
                                                                    amount=transaction.amount)
                if new_balance:
                    if recipient_new_balance is False:
                        context['message'] = 'insufficient fund'
                    else:
                        transaction.account_balance = new_balance
                        transaction.recipient_balance = recipient_new_balance
                        ams_service_provider.account_management_service().transfer(transaction)
                        context['message'] = 'transaction successful'
            else:
                context['message'] = 'incorrect pin'
        except Account.DoesNotExist as e:
            raise e


def __get_account_number_by_request(request: HttpRequest):
    account_dto = DepositAndWithdraw()
    account_dto.account_number = request.POST["account_number"]
    account_dto.account_pin = request.POST["account_pin"]
    account_dto.amount = request.POST["amount"]
    return account_dto


def __withdraw_if_post(request, context):
    if request.method == 'POST':
        try:
            transaction = __get_account_number_by_request(request)
            account_holder = ams_service_provider.account_holder_management_service().get_details_by_user(
                request.user.id)
            account = ams_service_provider.account_management_service().get_account_with_account_holder(
                account_holder.id)
            if account.account_pin == int(transaction.account_pin):
                new_balance = __get_new_balance(balance=account.account_balance, amount=transaction.amount,
                                                action='withdraw')
                if new_balance is False:
                    context['message'] = 'insufficient fund'
                else:
                    transaction.account_balance = new_balance
                    ams_service_provider.account_management_service().deposit_or_withdrawal(transaction)
                    context['message'] = 'transaction successful'
            else:
                context['message'] = 'incorrect pin'
        except Account.DoesNotExist as e:
            raise e


def __deposit_if_post(request, context):
    if request.method == 'POST':
        try:
            transaction = __get_account_number_by_request(request)
            account_holder = ams_service_provider.account_holder_management_service().get_details_by_user(
                request.user.id)
            account = ams_service_provider.account_management_service().get_account_with_account_holder(
                account_holder.id)
            if account.account_pin == int(transaction.account_pin):
                new_balance = __get_new_balance(balance=account.account_balance, amount=transaction.amount,
                                                action='deposit')
                if new_balance is False:
                    context['message'] = 'insufficient fund'
                else:
                    transaction.account_balance = new_balance
                    ams_service_provider.account_management_service().deposit_or_withdrawal(transaction)
                    context['message'] = 'transaction successful'
            else:
                context['message'] = 'incorrect pin'
        except Account.DoesNotExist as e:
            raise e


def __get_new_balance(balance: float, amount: float, action: str):
    if action == 'withdraw' or 'transfer':
        if float(amount) > balance:
            return False
        else:
            new_balance = balance - float(amount)
            return new_balance

    elif action == 'deposit':
        if float(amount) <= 0:
            return False
        else:
            new_balance = balance + float(amount)
            return new_balance


def __get_recipient_new_balance(balance: float, amount: float):
    if float(amount) <= 0:
        return False
    else:
        new_balance = balance + float(amount)
        return new_balance
