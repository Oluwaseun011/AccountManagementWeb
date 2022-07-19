from django.urls import path
from AMSapp.views.Profile import view

urlpatterns = [
    path('profile/', view.profile_view, name='profile'),

]