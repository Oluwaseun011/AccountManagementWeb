from django.urls import path
from AMSapp.views.Account import view

urlpatterns = [
    path('withdraw', view.withdrawal, name='withdraw'),
    path('deposit', view.deposit, name='deposit'),
    path('transfer', view.transfer, name='transfer')
]