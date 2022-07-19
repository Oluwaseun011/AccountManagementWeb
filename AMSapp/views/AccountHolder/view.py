from django.http import HttpRequest
from django.shortcuts import redirect, render
from AMSapp.service_provider import ams_service_provider
from AMSapp.dto.AccountHolderDto import *
from AMSapp.views.Account import view


def create_account_holder(request):
    context = {
        'title': 'Register'
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, 'account_holder/Register.html', context)


def list_account_holder(request):
    account_holders = ams_service_provider.account_holder_management_service().list_account_holders()
    context = {
        'tittle': 'List of Account Holders',
        'account_holders': account_holders
    }
    return render(request, 'account_holder/List.html', context)


def account_holder_details(request, account_holder_id: int):
    account_holder = ams_service_provider.account_holder_management_service().account_holder_details(account_holder_id)
    context = {
        'account_holder': account_holder
    }
    return render(request, '', context)


def edit_account_holder(request, account_holder_id: int):
    account_holder = ams_service_provider.account_holder_management_service().account_holder_details(account_holder_id)
    context = {
        'account_holder': account_holder,
        "take_off_time": account_holder.date_of_birth.strftime("%Y-%m-%d %H:%M:%S")
    }
    __edit_if_post_method(request, context, account_holder_id)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, 'account_holder/Edit.html', context)


def __get_attribute_from_request(request: HttpRequest):
    register_account_holder_dto = RegisterAccountHolder()
    register_account_holder_dto.username = request.POST['username']
    register_account_holder_dto.first_name = request.POST['first_name']
    register_account_holder_dto.last_name = request.POST['last_name']
    register_account_holder_dto.email = request.POST['email']
    register_account_holder_dto.address = request.POST['address']
    register_account_holder_dto.date_of_birth = request.POST['date_of_birth']
    register_account_holder_dto.phone_number = request.POST['phone_number']
    register_account_holder_dto.sex = request.POST['sex']
    register_account_holder_dto.password = request.POST['password']
    register_account_holder_dto.confirm_password = request.POST['confirm_password']
    return register_account_holder_dto


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            account_holder = __get_attribute_from_request(request)
            if account_holder.password == account_holder.confirm_password:
                account_holder_id = ams_service_provider.account_holder_management_service().create_account_holder(
                    account_holder)
                view.create_account_if_post_method(request, account_holder_id, context)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e


def __get_attribute_from_request_for_edit(request):
    edit_account_holder_dto = EditAccountHolder()
    edit_account_holder_dto.email = request.POST['email']
    edit_account_holder_dto.address = request.POST['address']
    edit_account_holder_dto.username = request.POST['username']
    edit_account_holder_dto.phone_number = request.POST['phone_number']
    edit_account_holder_dto.last_name = request.POST['last_name']
    edit_account_holder_dto.first_name = request.POST['first_name']
    edit_account_holder_dto.sex = request.POST['sex']
    edit_account_holder_dto.date_of_birth = request.POST['date_of_birth']
    return edit_account_holder_dto


def __edit_if_post_method(request, context, account_holder_id: int):
    if request.method == 'POST':
        try:
            account_holder = __get_attribute_from_request_for_edit(request)
            ams_service_provider.account_holder_management_service().edit_account_holder(account_holder_id,
                                                                                         account_holder)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e
