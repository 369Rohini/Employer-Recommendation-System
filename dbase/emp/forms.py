from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.models import User
from .models import *


class studentform(ModelForm):
    class Meta:
        model=student
        fields='__all__'
        exclude=['user','status']
        help_texts={
            'about':'Maximum characters limits : 2000',
            'github':'Format : https://github.com/<xyz>',
            'Linkedin':'Format : https://www.linkedin.com/in/<xyz>',
        }
        widgets:{
        'upload_your_work':forms.FileInput,
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class companyform(ModelForm):
    class Meta:
        model=employer
        fields='__all__'
        exclude=['user',]

class postjobform(ModelForm):
    class Meta:
        model=jobs
        fields='__all__'
        exclude = ['employer','status', ]


