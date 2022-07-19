from django.urls import path
from AMSapp.views.Loan import view

urlpatterns = [
    path('get_loan', view.get_loan, name='get_loan'),
    path('pay_loan', view.pay_loan, name='pay_loan')
]