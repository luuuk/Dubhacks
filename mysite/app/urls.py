from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # /resources
    path('resources', views.resources, name='resources'),
    path('file_a_report', views.questions, name='Info'),
    path('sign_in', views.emailver, name='Verify Email'),
    path('action', views.assaultaction, name='What Happened'),
    path('attributes', views.attributecollection, name='Perpetrator Details'),
    path('attrMatch', views.attrmatch, name='Perpetrator Match'),
    path('advisorConnect', views.advisorconnect, name='Connect with an Advisor'),

    path('login', views.login, name='Login'),
    path('match', views.match, name='Match')

]
