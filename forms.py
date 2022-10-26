from dataclasses import fields
from django import forms
from demoapp.models import *
import datetime

class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '__all__'
        
