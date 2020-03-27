from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Event


class DateInput(forms.DateInput):
    input_type = 'date'


class EventCreationForm(forms.ModelForm):

    class Meta: 
        model = Event
        fields = ['date','location','description','photo','host']
        widgets = {'host': forms.HiddenInput()}

        # host = models.OneToOneField(User, on_delete=models.CASCADE)





