from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Customer
        fields = '__all__'