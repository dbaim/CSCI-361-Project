from django import forms
from djangoapp.models import doctModel
from djangoapp.models import PatientModel
from djangoapp.models import AppointmentModel


class doctForms(forms.ModelForm):
    class Meta:
        model = doctModel
        fields="__all__"


class PatientForms(forms.ModelForm):
    class Meta:
        model = PatientModel
        fields="__all__"


class AppointmentForms(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        fields = "__all__"
