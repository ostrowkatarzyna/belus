from django import forms

from .models import *

class GraTworzForm(forms.ModelForm):
    class Meta:
        model = Gra
        fields =[]

class GraTworzGraczyForm(forms.Form):
    nazwa = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Wpisz imię"}))