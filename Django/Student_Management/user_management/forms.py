from django import forms
from django.core.exceptions import ValidationError
from user_management.models import *
from django.contrib.auth.models import User, Group


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    #role = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['username',
                  'password']

        label = {
            'password': 'Password'
        }

    def save(self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.set_password(password)
        u.save()
        return u


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user','profilerole']

class AttendanceForm(forms.ModelForm):
    grouprole = Group.objects.all()[3]
    students = Profile.objects.filter(profilerole=grouprole)
    student_list = []
    #print(students)
    for student in students:
        #print(student)

        student_list.append((student.rollnumber, str(student.rollnumber)+' '+student.firstname))

    studentList = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=student_list)

    class Meta:
        model = Attendance
        fields = ['completeDateTime', 'studentList']
        widgets = {
            'completeDateTime': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }