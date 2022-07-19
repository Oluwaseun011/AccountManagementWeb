from django.contrib import admin
from AMSapp.models import *
# Register your models here.

admin.site.register(AccountHolder)
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(Overdraft)
admin.site.register(Manager)