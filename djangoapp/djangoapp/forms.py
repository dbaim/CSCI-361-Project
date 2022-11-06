from django import forms
from djangoapp.models import doctModel
from djangoapp.models import PatientModel


class doctForms(forms.ModelForm):
    class Meta:
        model = doctModel
        fields="__all__"


class PatientForms(forms.ModelForm):
    class Meta:
        model = PatientModel
        fields="__all__"