from django import forms
from django.core.validators import RegexValidator
from django.core import validators
from django.contrib import messages
import re

class ctl_Saarthi1_app1_loginForm(forms.Form):
     email_id=forms.EmailField(max_length=40,required=True,validators=[RegexValidator(regex=r'^[a-zA-Z0-9]*$',message=('email_id must be Alphanumeric'),),])
     password=forms.CharField(max_length=20)