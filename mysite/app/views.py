from django.shortcuts import render
from .forms import loginForm


def index(request):
    return render(request, 'app/index.html')


def resources(request):
    return render(request, 'app/resources.html')


def questions(request):
    return render(request, 'app/question.html')


def emailver(request):
    return render(request, 'app/emailVer.html')


def assaultaction(request):
    return render(request, 'app/assaultAction.html')


def attributecollection(request):
    return render(request, 'app/attrCol.html')


def advisorconnect(request):
    return render(request, 'ADCONNECT NAME')


def attrmatch(request):
    return render(request, 'ATTRMATCH NAME')


def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            return render(assaultaction(request))

    return render(request, 'app/login.html')


def match(request):
    return render(request, 'app/match.html')

def case(request):
    return render(request, 'app/case.html')
