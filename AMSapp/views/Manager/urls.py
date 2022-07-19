from django.urls import path
from AMSapp.views.Manager import view

urlpatterns = [
    path('register', view.create_manager, name='register_manager'),
    path('edit_manager/<int:manager_id>', view.edit_manager, name='edit_manager'),
    path('manager_details/<int:manager_id>', view.manager_details, name='manager_details'),
    path('list_manager', view.list_manager, name='list_managers')
]