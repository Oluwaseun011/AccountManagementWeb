from django.http import HttpRequest
from django.shortcuts import redirect, render

from AMSapp.models import Loan
from AMSapp.service_provider import ams_service_provider
from AMSapp.dto.LoanDto import *
from AMSapp.views.Account import view

loan_types = {
    'car': 20000,
    'house': 30000,
    'education': 40000,
    'emergency': 5000
}


def get_loan(request):
    context = {

    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("profile")
    return render(request, 'loan/get_loan.html', context)


def pay_loan(request):
    context = {

    }
    __pay_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("profile")
    return render(request, 'loan/pay_loan.html', context)


def __get_pay_loan_attribute_from_request(request: HttpRequest):
    pay_loan_dto = PayLoan()
    pay_loan_dto.account_number = request.POST['account_number']
    pay_loan_dto.account_pin = request.POST['account_pin']
    pay_loan_dto.amount = request.POST['amount']
    return pay_loan_dto


def __pay_if_post_method(request, context):
    if request.method == 'POST':
        try:
            payment = __get_pay_loan_attribute_from_request(request)
            loan = __check_if_any_active_loan(payment.account_number)
            if loan:
                if loan.account_pin == int(payment.account_pin):
                    payment.loan_balance = __get_new_balance(amount=payment.amount, balance=loan.loan_balance)
                    if payment.loan_balance == 0:
                        payment.loan_status = 'inactive'
                    else:
                        payment.loan_status = 'active'
                    payment.loan_id = loan.loan_id
                    ams_service_provider.loan_management_service().pay_loan(payment)
                    context['saved'] = True
                else:
                    context['saved'] = False
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e


def __get_new_balance(amount: float, balance: float):
    if float(amount) <= 0:
        return False
    else:
        new_balance = balance - float(amount)
        return new_balance


def __get_loan_attribute_from_request(request: HttpRequest):
    get_loan_dto = GetLoan()
    get_loan_dto.account_number = request.POST['account_number']
    get_loan_dto.loan_type = request.POST['loan_type']
    get_loan_dto.account_pin = request.POST['account_pin']
    return get_loan_dto


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            loan = __get_loan_attribute_from_request(request)
            account = ams_service_provider.account_management_service().get_account_with_account_number(
                account_number=loan.account_number)
            try:
                if account.account_pin == int(loan.account_pin):
                    if_active = __check_if_any_active_loan(loan.account_number)
                    if not if_active:
                        loan.loan_amount = __get_loan_amount_by_type(loan.loan_type)
                        loan.loan_balance = loan.loan_amount
                        loan.account_id = account.id
                        loan.loan_status = "active"
                        ams_service_provider.loan_management_service().get_loan(loan)

                        context['saved'] = True
                else:
                    context['saved'] = False
            except Exception as e:
                context['saved'] = False
                raise e
        except Exception as e:
            context['saved'] = False
            raise e


def __get_loan_amount_by_type(loan_type: str):
    for loan in loan_types:
        if loan == loan_type:
            val = loan_types[loan]
            return val
    return None


def __check_if_any_active_loan(account_number: str) -> ListLoan:
    loans: list = ams_service_provider.loan_management_service().list_loan_by_account_number(account_number)
    for loan in loans:
        if loan.loan_status == 'active':
            return loan
