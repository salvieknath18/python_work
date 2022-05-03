from django.shortcuts import render
from poll.models import *
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    context = {}
    context['title'] = 'Polls'
    context['questions'] = Question.objects.all()
    #return HttpResponse('hello')
    return render(request, 'poll/index.html', context)

@login_required(login_url='/login/')
def details(request, id):
    context = {}
    context['title'] = 'Poll Details'
    try :
        context['question'] = Question.objects.get(id=id)
    except:
        raise Http404
    return render(request, 'poll/details.html', context)

@login_required(login_url='/login/')
def poll_ans(request, id=None):
    if request.method == 'GET':
        context = {}
        context['title'] = 'Poll Details'
        try:
            context['question'] = Question.objects.get(id=id)
        except:
            raise Http404
        return render(request, 'poll/poll.html', context)

    if request.method == 'POST':
        data = request.POST
        userid = 1
        ret = Answer.objects.create(user_id=userid, choice_id=data['choice'])
        #in answer foreign key User and choice, to access id of user and choice underscore used
        #eg. user_id = 1, choice_id = choiceid
        #to access other parameters of user user__parameter(double underscore)
        if ret:
            return HttpResponse("Your vote is done successfully")
        else:
            return HttpResponse("Your vote is Not Done")