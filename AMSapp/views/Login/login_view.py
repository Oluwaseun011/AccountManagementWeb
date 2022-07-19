from django.contrib.sessions import serializers
from django.core.serializers import serialize
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from AMSapp.service_provider import ams_service_provider


def login_get(request):
    context = {
        'next': request.GET.get("next", 'profile')
    }
    return render(request, 'home.html', context)


def login_post(request):
    context = dict()
    resolve_url = request.GET.get("next")
    username = request.POST.get('username')
    password = request.POST.get('password')
    user: User = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        groups = serialize('json', request.user.groups.all())
        if 'AccountHolder' in groups:
            account = serialize('json', list(ams_service_provider.account_holder_management_service().get_details_by_user(request.user.id)))

            request.session.__setitem__("account", account)
        elif 'Manager' in groups:
            manager = ams_service_provider.manager_management_service().manager_details(request.user.id)
            manager = serialize('json', manager)
            request.session['manager'] = manager
        request.session['groups'] = groups
        return redirect(resolve_url)
    else:
        context['message'] = 'username or password incorrect'
        return render(request, 'home.html', context)


def log_out(request):
    logout(request)
    return redirect("home")


def change_password(request, user_id: int):
    pass
