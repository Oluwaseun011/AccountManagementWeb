from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.serializers import serialize, deserialize

from AMSapp.service_provider import ams_service_provider


@login_required(redirect_field_name='next')
def profile_view(request):
    groups = request.session.get("groups")
    account = request.session.get("account")

    if "AccountHolder" in groups:

        context = {
            'account_holder': account

        }
        return render(request, 'profile.html', context)
    elif "Manager" in groups:
        user_id = request.user.id
        # manager = ams_service_provider.manager_management_service().get_details_by_user(user_id)

        context = {
            'manager': "manager"

        }
        return render(request, 'managerprofile.html', context)
