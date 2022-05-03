from django import forms
import requests
from datetime import date

class RestaurantForm(forms.Form):
    userlist = requests.get('http://127.0.0.1:8000/api/users/').json()
    print(userlist)
    userchoice = []
    for u in userlist:
        userchoice.append((u['id'],u['username']))
    name = forms.CharField()
    street = forms.CharField()
    number = forms.IntegerField()
    city = forms.CharField()
    zipCode = forms.CharField()
    stateOrProvince = forms.CharField()
    country = forms.CharField()
    telephone = forms.CharField()
    url = forms.URLField()
    #userchoice = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    user = forms.ChoiceField(choices=userchoice)
    date = forms.DateField()

    def __unicode__(self):
        return u"%s" % self.name

class DishForm(forms.Form):
    userlist = requests.get('http://127.0.0.1:8000/api/users/').json()
    userchoice = []
    for u in userlist:
        userchoice.append((u['id'], u['username']))
    restaurantlist = requests.get('http://127.0.0.1:8000/api/restaurants/').json()
    restaurantchoice = []
    for u in restaurantlist:
        restaurantchoice.append((u['id'], u['name']))
    name = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    #user = forms.ForeignKey(User, default=1,on_delete=models.CASCADE)
    user = forms.ChoiceField(choices=userchoice)
    date = forms.DateField()
    image = forms.ImageField()
    #restaurant = forms.ForeignKey(Restaurant, null=True, related_name='dishes',on_delete=models.CASCADE)
    restaurant = forms.MultipleChoiceField(choices=restaurantchoice)

    def __unicode__(self):
        return u"%s" % self.name

class ReviewForm(forms.Form):
    userlist = requests.get('http://127.0.0.1:8000/api/users/').json()
    userchoice = []
    for u in userlist:
        userchoice.append((u['id'], u['username']))
    restaurantlist = requests.get('http://127.0.0.1:8000/api/restaurants/').json()
    restaurantchoice = []
    for u in restaurantlist:
        restaurantchoice.append((u['id'], u['name']))
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = forms.ChoiceField(choices=RATING_CHOICES)
    comment = forms.CharField()
    #user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    user = forms.ChoiceField(choices=userchoice)
    date = forms.DateField()
    #restaurant = models.ManyToManyField(Restaurant,blank=True,default=1)
    restaurant = forms.ChoiceField(choices=restaurantchoice)

#class RestaurantReview(Review):
 #   restaurant = models.ManyToManyField(Restaurant,blank=True,default=1)
