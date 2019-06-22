from django import forms
from . import models

class inputAnswer(forms.Form):
    answer= forms.CharField(label='',max_length=100,required=True)