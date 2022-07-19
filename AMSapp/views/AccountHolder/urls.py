from django.urls import path
from AMSapp.views.AccountHolder import view

urlpatterns = [
    path('register', view.create_account_holder, name='register_account_holder'),
    path('edit_account_holder/<int:account_holder_id>', view.edit_account_holder, name='edit_account_holder'),
    path('account_holder_details/<int:account_holder_id>', view.account_holder_details, name='account_holder_details'),
    path('list_account_holder', view.list_account_holder, name='list_account_holders')
]