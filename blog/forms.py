from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from .models import Event



class EventCreationForm(ModelForm):

    class Meta: 
        model = Event
        fields = ['date','location','description']



