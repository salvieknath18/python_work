from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutor
from django.http import JsonResponse
from .serializers import TutorSerializer
from rest_framework import generics

from rest_framework import viewsets


class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


class TutorList(generics.ListCreateAPIView):  # allowed only GET, POST, HEAD, OPTIONS
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer


def home(request):
    return HttpResponse('hello')
