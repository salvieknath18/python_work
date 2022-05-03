from django.shortcuts import render, redirect, HttpResponseRedirect
import requests
from .form import *

# Create your views here.


def homepage(request):
    homelist = requests.get('http://127.0.0.1:8000/api/').json()
    return render(request, 'home.html', {"content": homelist})


def restaurants(request):
    restaurantsList = requests.get('http://127.0.0.1:8000/api/restaurants').json()
    form = RestaurantForm()
    return render(request, 'restaurant.html', {"restaurantsList": restaurantsList, "form":form})


def restaurantsCRUD(request,urlmethod,id):
    if request.method == 'GET':
        if urlmethod == 'get':
            restaurantget = requests.get('http://127.0.0.1:8000/api/restaurants/'+str(id)).json()
            return render(request, 'restaurantDetails.html', {"restaurant": restaurantget})
        if urlmethod == 'delete':
            requests.delete('http://127.0.0.1:8000/api/restaurants/'+str(id))
        if urlmethod == 'update':
            restaurant = requests.get('http://127.0.0.1:8000/api/restaurants/'+str(id)).json()
            form = RestaurantForm(restaurant)
            return render(request, 'restaurantUpdate.html', {"form": form, "uid": id})
        return HttpResponseRedirect('http://127.0.0.1:9000/restaurants/')
    if request.method == 'POST':
        print(request.POST)
        if urlmethod == 'add':
            requests.post('http://127.0.0.1:8000/api/restaurants/',data = request.POST)
        if urlmethod == 'update':
            requests.put('http://127.0.0.1:8000/api/restaurants/'+str(id)+'/',data = request.POST)
        return HttpResponseRedirect('http://127.0.0.1:9000/restaurants/')

def dishes(request):
    dishesList = requests.get('http://127.0.0.1:8000/api/dishes').json()
    form = DishForm()
    restaurantsList = requests.get('http://127.0.0.1:8000/api/restaurants').json()
    restaurantsidname = {}
    for rest in restaurantsList:
        restaurantsidname[rest['id']]=rest['name']
    print(dishesList)
    return render(request, 'dish.html', {"dishesList": dishesList, "form":form, "restaurantsidname": restaurantsidname})


def dishesCRUD(request,urlmethod,id):
    if request.method == 'GET':
        if urlmethod == 'get':
            dishget = requests.get('http://127.0.0.1:8000/api/dishes/'+str(id)).json()
            return render(request, 'dishDetails.html', {"dish": dishget})
        if urlmethod == 'delete':
            requests.delete('http://127.0.0.1:8000/api/dishes/'+str(id))
        if urlmethod == 'update':
            restaurant = requests.get('http://127.0.0.1:8000/api/dishes/'+str(id)).json()
            form = RestaurantForm(restaurant)
            return render(request, 'dishUpdate.html', {"form": form, "uid": id})
        return HttpResponseRedirect('http://127.0.0.1:9000/dishes/')
    if request.method == 'POST':
        print(request.POST)
        if urlmethod == 'add':
            requests.post('http://127.0.0.1:8000/api/dishes/', data=request.POST)
        if urlmethod == 'update':
            requests.put('http://127.0.0.1:8000/api/dishes/'+str(id)+'/', data=request.POST)
        return HttpResponseRedirect('http://127.0.0.1:9000/dishes/')
    


def restaurantReview(request,id):
    reviewList = requests.get('http://127.0.0.1:8000/api/restaurantsreviews').json()
    print(reviewList)
    reviewListn = []
    for item in reviewList:
        print(item['restaurant'],id)
        if item['restaurant'] == id:
            reviewListn.append(item)
    print(reviewListn)
    form = ReviewForm()
    restaurantinfo = requests.get('http://127.0.0.1:8000/api/restaurants/'+str(id)).json()
    return render(request, 'review.html', {"form":form, "reviewList": reviewListn, 'restName':restaurantinfo['name']})

