from django.shortcuts import render
from django.core.mail import send_mail
from .forms import caseForm
from .models import Report

def index(request):
    print("Begun reporting")
    """
    for i in range(2):
        send_mail('This is a test',
        'Im watching you...',
        'save2019@hushmail.com',
        ['serenagilani@comcast.net'],
        fail_silently=False)
    """
    return render(request, 'app/index.html')


def mockIP():
    return 12356765435654


def getID(Report):
    return Report.id


def confidentiality(request):
    if request.method == 'POST':
        print("collecting ip data")
        report = Report()
        report.save()
        print(report.id)
    return render(request, 'app/confidentiality.html')


def resources(request):
    return render(request, 'app/resources.html')

def resourcesT(request):
    return render(request, 'app/resources.html', {'submitted': 'TRUE'})


def questions(request):
    return render(request, 'app/question.html')


def emailver(request):
    return render(request, 'app/emailVer.html')


def case(request, pk):
    report = Report #get_object_or_404(Report, pk=pk)

    if request.method == 'POST':
    #if 'do_something' in request.POST:
        form = caseForm(request.POST)
        if form.is_valid():
            form.save()

    context= {'form': form}

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

def case(request):
    return render(request, 'app/case.html')

def confidentiality(request):
    return render(request, 'app/confidentiality.html')