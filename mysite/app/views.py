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
        request.session['id'] = report.id
        return render(request, 'app/case.html')
    return render(request, 'app/case.html', {'form': form})


def attributecollection(request):
    id = request.session.get('id', None)
    report = Report.objects.filter(id=id)
    if request.method == 'POST':
        form = caseForm(request.POST or None)
        if form.is_valid():
            form.save()
            report.case_type=form["case_type"]
            report.date=form["date"]
            report.description=form["description"]
            print(report.description)
            return render(request, 'app/attrCol.html')
    return render(request, 'app/attrCol.html')


def resources(request):
    print("received to resources")
    return render(request, 'app/resources.html')


def resourcesT(request):
    print("Received request to resourcesT")
    reps = Report.objects.all()
    single = reps[len(reps) - 3]
    try:
        address = single.uwnetid + "@uw.edu"
        send_mail('Hi there, this email is to notify you of an update related to your SAVE report',
                  'Please visit http://127.0.0.1:8080/',
                  'save2019@hushmail.com',
                  [address],
                  fail_silently=False)
    except TypeError:
        pass

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