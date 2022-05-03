from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status

from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer

from rest_framework import generics

from django.contrib.auth import authenticate

'''
********************  Using viewsets and router URL  ((Implementation of poll requests 4))
                  This replaces the two classes of polls reduces the code
'''

from rest_framework import viewsets


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer



'''
********************  Using Generics API view of rest framework ((Implementation of poll requests 3))
'''


class PollList3(generics.ListCreateAPIView):  # allowed only GET, POST, HEAD, OPTIONS
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail3(generics.RetrieveDestroyAPIView):  # allowed GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):  # allowed only GET, POST, HEAD, OPTIONS
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer


class CreateVote(APIView):  # allowed only post and option
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

'''
*****************    Using API view not using generics ((Implementation of poll requests 2))
'''
from rest_framework.views import APIView


class PollList2(APIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data)


class PollDetail2(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data)


'''
********************* Sending response Without Serializer  ((Implementation of poll requests 1))
if we are not using rest framework simple code as follows 
'''

from django.http import JsonResponse

def polls_list1(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by", "pub_date"))}
    return JsonResponse(data)

def polls_detail1(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
    "question": poll.question,
    "created_by": poll.created_by.username,
    "pub_date": poll.pub_date
    }}
    return JsonResponse(data)

'''
We have seen 4 ways to build API views until now
    • Pure Django views ((Implementation of poll requests 1))
    • APIView subclasses ((Implementation of poll requests 2))
    • generics.* subclasses ((Implementation of poll requests 3))
    • viewsets.ModelViewSet ((Implementation of poll requests 4))
So which one should you use when? My rule of thumb is,
    • Use viewsets.ModelViewSet when you are goin to allow all or most of CRUD operations on a model.
    • Use generics.* when you only want to allow some operations on a model
    • Use APIView when you want to completely customize the behaviour.
'''

