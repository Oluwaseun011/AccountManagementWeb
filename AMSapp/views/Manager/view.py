from django.http import HttpRequest
from django.shortcuts import redirect, render
from AMSapp.service_provider import ams_service_provider
from AMSapp.dto.ManagerDto import *


def create_manager(request):
    context = {
        'title': 'Register'
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, 'manager/Register.html', context)


def list_manager(request):
    managers = ams_service_provider.manager_management_service().list_managers()
    context = {
        'tittle': 'List of Managers',
        'account_holders': managers
    }
    return render(request, 'manager/List.html', context)


def manager_details(request, manager_id: int):
    manager = ams_service_provider.manager_management_service().account_holder_details(manager_id)
    context = {
        'manager': manager
    }
    return render(request, '', context)


def edit_manager(request, manager_id: int):
    manager = ams_service_provider.manager_management_service().manager_details(manager_id)
    context = {
        'manager': manager,
        "take_off_time": manager.date_of_birth.strftime("%Y-%m-%d %H:%M:%S")
    }
    __edit_if_post_method(request, context, manager_id)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, 'manager/Edit.html', context)


def __get_attribute_from_request(request: HttpRequest):
    register_manager_dto = RegisterManager()
    register_manager_dto.username = request.POST['username']
    register_manager_dto.first_name = request.POST['first_name']
    register_manager_dto.last_name = request.POST['last_name']
    register_manager_dto.email = request.POST['email']
    register_manager_dto.address = request.POST['address']
    register_manager_dto.date_of_birth = request.POST['date_of_birth']
    register_manager_dto.phone_number = request.POST['phone_number']
    register_manager_dto.password = request.POST['password']
    register_manager_dto.confirm_password = request.POST['confirm_password']
    return register_manager_dto


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            manager = __get_attribute_from_request(request)
            if manager.password == manager.confirm_password:
                ams_service_provider.manager_management_service().create_manager(manager)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e


def __get_attribute_from_request_for_edit(request):
    edit_manager_dto = EditManager()
    edit_manager_dto.email = request.POST['email']
    edit_manager_dto.address = request.POST['address']
    edit_manager_dto.username = request.POST['username']
    edit_manager_dto.phone_number = request.POST['phone_number']
    edit_manager_dto.last_name = request.POST['last_name']
    edit_manager_dto.first_name = request.POST['first_name']
    edit_manager_dto.date_of_birth = request.POST['date_of_birth']
    return edit_manager_dto


def __edit_if_post_method(request, context, manager_id: int):
    if request.method == 'POST':
        try:
            manager = __get_attribute_from_request_for_edit(request)
            ams_service_provider.manager_management_service().edit_manager(manager_id, manager)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e