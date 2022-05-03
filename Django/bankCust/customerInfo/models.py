from django.db import models


class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    customerAge = models.IntegerField()
    profileImage = models.ImageField(upload_to="customerImages", blank=True, null=True)

    def __str__(self):
        return self.customerName


class Account(models.Model):
    accountTypeChoices = (('SB','Savings'),('LB','Loan'),('IB','Insurance'))
    accountNumber = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name="accounts", on_delete=models.CASCADE)
    accountBalance = models.DecimalField('Indian amount', max_digits=8, decimal_places=2, blank=True, null=True)
    accountType = models.CharField(max_length=10, choices=accountTypeChoices)

    def __str__(self):
        return self.accountType
