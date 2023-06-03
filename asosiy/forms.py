from .models import *
from django import forms


class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields ='__all__'


class YonalishForm(forms.Form):
    nom = forms.CharField(max_length=70)
    aktiv = forms.BooleanField()






