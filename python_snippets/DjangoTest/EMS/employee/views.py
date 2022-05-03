from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from employee.models import *
from employee.forms import *
from EMS.decorators import role_required

def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            context['error'] = 'Invalid Credentials'
            return render(request, 'auth/login.html', context=context)
    else:
        return render(request, 'auth/login.html', context=context)


@login_required(login_url='/login/')
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'auth/success.html', context=context)

@login_required(login_url='/login/')
def user_logout(request):
    context = {}
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url='/login/')
def employee_list(request):
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employees'
    #return HttpResponse('hello')
    return render(request, 'employee/index.html', context)

@login_required(login_url='/login/')
def employee_details(request, id=None):
    context = {}
    context['user'] = get_object_or_404(User, id=id)
    print(get_object_or_404(User, id=id))
    return render(request, 'employee/details.html', context)

@login_required(login_url='/login/')
@role_required(allowed_roles=['Admin','HR'])
def employee_add(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            u = user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'employee/add.html', context)

@login_required(login_url='/login/')
@role_required(allowed_roles=['Admin','HR'])
def employee_edit(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request, 'employee/edit.html', {"user_form": user_form})
    else:
        user_form = UserForm(instance=user)
        return render(request, 'employee/edit.html', {"user_form": user_form})

@login_required(login_url='/login/')
@role_required(allowed_roles=['Admin','HR'])
def employee_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'employee/delete.html', context)

from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class ProfileUpdate(UpdateView):
    fields = ['designation', 'salary', 'picture']
    template_name = 'auth/profile_update.html'
    success_url = reverse_lazy('my_profile')

    def get_object(self):
        return self.request.user.profile



class MyProfile(DetailView):
    template_name = 'auth/profile.html'

    def get_object(self):
        return self.request.user.profile