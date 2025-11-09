from django import forms
from django.forms import EmailField
from .models import *

class inputForm(forms.ModelForm):
    url = EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Any URL.......'}))

    class Meta:
        model = Mail
        fields = ['url']