from django.http import HttpResponse
from django.template import loader
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

