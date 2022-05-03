from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from .models import *
from .serializer import *
import decimal
from rest_framework import generics
from rest_framework import viewsets, status
from django.http import HttpResponse
###hello

def home(request):
    return HttpResponse(r"<h1>Hello and Welcome to customer API<h1></br>Please Click for the documentation url:<a href='/docs/'>Swagger URL<a>")

class CustomerViewSet(viewsets.ModelViewSet):#add/update/delete/post
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


from rest_framework.views import APIView


class Transaction(APIView):  # allowed only post and option
    def post(self, request):
        accountNumber = request.data.get("accountNumber")
        transactionAmount = decimal.Decimal(request.data.get("transactionAmount"))
        transactionMethod = request.data.get("transactionMethod")
        customerAccount = Account.objects.filter(accountNumber=accountNumber)
        customerAmount = customerAccount[0].accountBalance
        print(customerAmount)
        if transactionMethod == "D":
            customerAmount = customerAmount + transactionAmount
        elif transactionMethod == "W":
            customerAmount = customerAmount - transactionAmount

        account_serializer = AccountSerializer(customerAccount[0],
                                         data={"accountBalance": customerAmount, "accountType": customerAccount[0].accountType, "customer": customerAccount[0].customer.pk})

        if account_serializer.is_valid():
            account = account_serializer.save()
            return Response(account_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''
        return Response(customerAmount, status=status.HTTP_201_CREATED)
        '''