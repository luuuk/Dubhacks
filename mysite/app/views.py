from django.shortcuts import render
from .forms import caseForm
from .models import Report


def index(request):
    return render(request, 'app/index.html')


def resources(request):
    return render(request, 'app/resources.html')


def questions(request):
    return render(request, 'app/question.html')


def emailver(request):
    return render(request, 'app/emailVer.html')


def assaultaction(request):
    form= caseForm(request.POST or None)
    if 'do_something' in request.POST:
        form.save()

    context= {'form': form }

    return render(request, 'app/case.html', context)


def attributecollection(request):
    return render(request, 'app/attrCol.html')


def advisorconnect(request):
    return render(request, 'ADCONNECT NAME')


def attrmatch(request):
    return render(request, 'ATTRMATCH NAME')


def login(request):


    return render(request, 'app/login.html')


def match(request):
    return render(request, 'app/match.html')

