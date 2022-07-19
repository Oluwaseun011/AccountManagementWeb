import datetime

from django.contrib.auth.models import User
from django.db import models


class AccountHolder(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, default=None)
    date_of_birth = models.DateField()
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)

    def __str__(self):
        return f"{self.user.first_name}\t{self.phone_number}\t{self.address}"


class Account(models.Model):
    account_holder = models.ForeignKey(AccountHolder, on_delete=models.RESTRICT)
    account_number = models.CharField(max_length=10)
    account_pin = models.IntegerField(max_length=4)
    account_balance = models.FloatField(max_length=500)
    account_status = models.CharField(default='active', max_length=10)
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)


class Loan(models.Model):
    account = models.ForeignKey(Account, on_delete=models.RESTRICT)
    loan_balance = models.FloatField(max_length=500)
    loan_status = models.CharField(default='active', max_length=20)
    loan_type = models.CharField(max_length=20)
    loan_amount = models.FloatField(max_length=500)
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)


class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)


class Overdraft(models.Model):
    account = models.ForeignKey(Account, on_delete=models.RESTRICT)
    overdraft_amount = models.FloatField(max_length=500)
    overdraft_balance = models.FloatField(max_length=500)
    overdraft_status = models.CharField(default='active', max_length=20)
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)
