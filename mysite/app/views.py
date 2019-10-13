from django.shortcuts import render


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

