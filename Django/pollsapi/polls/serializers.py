from rest_framework import serializers
from .models import Poll, Choice, Vote
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class VoteSerializer(serializers.ModelSerializer):
    class Meta: model = Vote
    fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
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

'''
**************************   Use of Serializer object  tested on Shell  *******************       

(DjangoEnv) C:\\Users\piyuekka\Desktop\Target\Target\Django\pollsapi>python manage.py shell
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls.serializers import PollSerializer
>>> from polls.models import Poll
>>> poll_serializer = PollSerializer(data={"question": "Mojito or Caipirinha?",
...
...
KeyboardInterrupt
>>> poll_serializer = PollSerializer(data={"question": "Mojito or Caipirinha?","created_by": 1}) # This to add
>>> poll_serializer.is_valid()
True
>>> poll = poll_serializer.save()
>>> poll.pk
5
>>>
>>> poll_serializer = PollSerializer(instance=poll, data={"question": "Mojito, Caipirinha or margarita?", "created_by": 1}) 
vTrue
>>> poll_serializer.save()
<Poll: Mojito, Caipirinha or margarita?>
>>> Poll.objects.get(pk=5).question
'Mojito, Caipirinha or margarita?'
'''