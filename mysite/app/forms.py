from django import forms
from .models import Report

class loginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password')

class caseForm(forms.Form):
    class Meta:
        model = Report
        fields = ["id", "case_type", "date", "description"]


class agreeToTermsForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['id']