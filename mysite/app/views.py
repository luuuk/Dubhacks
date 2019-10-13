from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')


def resources(request):
    return render(request, 'app/resources.html')


def questions():
    return render(request, 'app/question.html')