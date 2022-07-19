"""AMSweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AMSapp.views.Home import view
from AMSapp.views.Login import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view.login_get, name='home'),
    # path('', view.home_view, name='home'),
    path('login/', include('AMSapp.views.Login.urls')),
    path('account_holder/', include('AMSapp.views.AccountHolder.urls')),
    path('manager/', include('AMSapp.views.Manager.urls')),
    path('profile/', include('AMSapp.views.Profile.urls')),
    path('account/', include('AMSapp.views.Account.urls')),
    path('loan/', include('AMSapp.views.Loan.urls')),
    path('overdraft/', include('AMSapp.views.Overdraft.urls'))
]