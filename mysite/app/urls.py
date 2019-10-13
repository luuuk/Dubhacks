from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # /resources
    path('resources', views.resources, name='resources'),
    path('resourcesT', views.resourcesT, name='resources'),
    path('fileareport', views.questions, name='Info'),
    path('signin', views.emailver, name='Verify Email'),
    path('confidentiality', views.confidentiality, name='Conf'),
    path('case', views.case, name='What Happened'),
    path('attributes', views.attributecollection, name='Perpetrator Details'),
    path('attrMatch', views.attrmatch, name='Perpetrator Match'),
    path('advisorConnect', views.advisorconnect, name='Connect with an Advisor'),
    path('login', views.login, name='Login'),
    path('match', views.match, name='Match'),
    path('attributeCollection', views.attributecollection, name="Attribute Collection"),


]
