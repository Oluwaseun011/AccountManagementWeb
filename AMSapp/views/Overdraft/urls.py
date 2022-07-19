from django.urls import path
from AMSapp.views.Overdraft import view

urlpatterns = [
    path('get_overdraft', view.get_overdraft, name='get_overdraft'),
]