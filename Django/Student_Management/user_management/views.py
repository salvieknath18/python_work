from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from Student_Management.decorators import role_required
from user_management.forms import *
from rest_framework import viewsets
from .serializers import *

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

def home(request):
    if request.user.username:
        if request.user.profile.profilerole.name == 'Student':
            return redirect('/details/' + str(request.user.id) + '/')
        return HttpResponseRedirect(reverse('user_list'))
    else:
        return HttpResponseRedirect(reverse('user_login'))
    #return HttpResponse('hello')

@login_required(login_url='/login/')
@role_required(allowed_roles=['Admin','Staff','Instructor'])
def user_list(request):
    #print(request.user.profile.profilerole)
    context = {}
    users = Profile.objects.all()
    grouprole = Group.objects.all()[3]
    context['usertype'] = 'Students'
    context['users'] = Profile.objects.filter(profilerole = grouprole)
    #return HttpResponse('hello')
    return render(request, 'user_management/index.html', context)

@login_required(login_url='/login/')
@role_required(allowed_roles=['Admin'])
def staff_list(request):
    #print(request.user.profile.profilerole)
    context = {}
    users = Profile.objects.all()
    grouprole = Group.objects.all()[1]
    context['usertype'] = 'Staff'
    context['users'] = Profile.objects.filter(profilerole = grouprole)
    #return HttpResponse('hello')
    return render(request, 'user_management/index.html', context)

@login_required(login_url='/login/')
@role_required(allowed_roles=['Admin','Staff'])
def instructor_list(request):
    #print(request.user.profile.profilerole)
    context = {}
    users = Profile.objects.all()
    grouprole = Group.objects.all()[2]
    context['usertype'] = 'Instructor'
    context['users'] = Profile.objects.filter(profilerole = grouprole)
    #return HttpResponse('hello')
    return render(request, 'user_management/index.html', context)

def user_add(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        context['user_form'] = user_form
        if user_form.is_valid():
            u = user_form.save()
            userprofile = get_object_or_404(Profile, user_id=u.id)
            profile_form = ProfileForm(instance=userprofile)
            return render(request, 'user_management/editp.html', {"user_form": profile_form, "id":u.id})
        else:
            return render(request, 'user_management/add.html', context)
    else:
        user_form = UserForm()
        context['user_form'] = user_form
        return render(request, 'user_management/add.html', context)

def profile_edit(request, id):
    user = get_object_or_404(Profile, user_id=id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            if request.user.profile.profilerole.name == 'Student':
                return redirect('/details/'+str(user.id)+'/')
            return HttpResponseRedirect(reverse('user_list'))
        else:
            return render(request, 'user_management/editp.html', {"user_form": profile_form, 'id':id})
    else:
        profile_form = ProfileForm(instance=user)
        return render(request, 'user_management/editp.html', {"user_form": profile_form, 'id':id})

@login_required(login_url='/login/')
def profile_details(request, id=None):
    context = {}
    context['userprofile'] = get_object_or_404(User, id=id)
    print(get_object_or_404(User, id=id))
    #return HttpResponse('hello')
    return render(request, 'user_management/details.html', context)

def user_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        if request.user.profile.profilerole.name == 'Student':
            user.delete()
            return redirect('/login/')
        print(type(user))
        user.delete()
        return HttpResponseRedirect(reverse('user_list'))
    else:
        context = {}
        context['userprofile'] = user
        return render(request, 'user_management/delete.html', context)

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
            if user.profile.profilerole.name == 'Student':
                return redirect('/details/'+str(user.id)+'/')
            return HttpResponseRedirect(reverse('user_list'))
        else:
            context['error'] = 'Invalid Credentials'
            return render(request, 'user_management/login.html', context=context)
    else:
        return render(request, 'user_management/login.html', context=context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

@login_required(login_url='/login/')
@role_required(allowed_roles=['Admin','Staff','Instructor'])
def student_attendance(request):
    context = {}
    if request.method == 'POST':
        attendanceForm = AttendanceForm(request.POST)
        context['attendanceForm'] = attendanceForm
        if attendanceForm.is_valid():
            attendanceForm.save()
            return HttpResponseRedirect(reverse('user_list'))
    else:
        attendanceForm = AttendanceForm()
        context['attendanceForm'] = attendanceForm
        return render(request, 'user_management/attendance.html', context)

@login_required(login_url='/login/')
@role_required(allowed_roles=['Admin','Staff'])
def student_attendance_record(request):
    context={}
    context['records'] = Attendance.objects.all()
    return render(request, 'user_management/records.html', context)

@login_required(login_url='/login/')
@role_required(allowed_roles=['Admin','Staff'])
def student_attendance_report(request):
    rollnumber = request.POST['rollnumber']
    print(rollnumber)
    context={}
    records = Attendance.objects.all()
    total_count = records.count()
    present_record = []
    for record in records:
        if rollnumber in record.studentList:
            present_record.append((record.completeDateTime).strftime('%m/%d/%Y'))
    present_count = len(present_record)
    percent_attendance = (present_count/total_count)*100
    print(percent_attendance)
    context['present_record'] = present_record
    context['percent_attendance'] = percent_attendance
    return render(request, 'user_management/report.html', context)
