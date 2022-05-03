from rest_framework import serializers
from .models import Tutor
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):  # We have overriden the ModelSerializer method’s create() to save the User instances.
        user = User(email=validated_data['email'],username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)  # Creating a Token While creating a User
        return user