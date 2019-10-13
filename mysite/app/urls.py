from django.urls import path
from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('resources', views.resources, name='resources'),
    path('file_a_report', views.questions, name='Info'),
]