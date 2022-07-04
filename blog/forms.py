from blog.models import *
from django import forms
from django.forms import ModelForm

class blogForm(ModelForm):
    class Meta:
        model=blogs
        fields='__all__'
        exclude=['likes','date']