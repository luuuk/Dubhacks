from django.shortcuts import render
from django.core.mail import send_mail
from .forms import caseForm, agreeToTermsForm
from .models import Report

def index(request):
    return render(request, 'app/index.html')


def mockIP():
    return 12356765435654


def getID(Report):
    return Report.id


def confidentiality(request):
    if request.POST:
        print("Begun reporting")
        return render(request, 'app/confidentiality.html')
    return render(request, 'app/confidentiality.html')


def case(request):
    initial = {'id': request.session.get('id', None)}
    form = agreeToTermsForm(request.POST or None, initial=initial)
    if request.method == 'POST':
        report = form.save(commit=False)
        report.save()
        print(report.id)
        print("collecting ip data for form")
        #print(form.id)
        #request.session['id'] = form.id

        return render(request, 'app/case.html')
    return render(request, 'app/case.html', {'form': form})


def attributecollection(request):
    form = caseForm(request.POST or None)
    print(form.auto_id)
    if request.method == 'POST':
        if form.is_valid():
            # report = form.save()
            return render(request, 'app/attrCol.html')
    return render(request, 'app/attrCol.html')


def resources(request):
    print("received to resources")
    return render(request, 'app/resources.html')


def resourcesT(request):
    print("Received request to resourcesT")

    """
    send_mail('This is a test',
              'Im watching you...',
              'save2019@hushmail.com',
              ['serenagilani@comcast.net'],
              fail_silently=False)
    """
    return render(request, 'app/resources.html', {'submitted': 'TRUE'})


def questions(request):
    return render(request, 'app/question.html')


def emailver(request):
    return render(request, 'app/emailVer.html')

def login(request):
    return render(request, 'app/login.html')


def match(request):
    allReports = Report.objects.all()
    numMatches = 0
    if allReports.count() > 0:
        thisReport = allReports[len(allReports) - 1]
        numMatches = thisReport.checkMatchSimple()


    if (numMatches):
        return render(request, 'app/match.html', {'Matches':numMatches})
    else:
        return render(request, 'app/match.html')