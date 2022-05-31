from django import forms
from django.forms import ModelForm
from .models import Applicant

# To create a Applicant form,
class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ('name', 'address', 'zip_code','phone', 'web', 'gender', 'email_address')

        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'gender': '',
            'email_address': ''
        }
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Applicant Name'}),
        'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
        'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zip Code'}),
        'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone'}),
        'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Address'}),
        'gender': forms.Select(attrs={'class': 'form-control'}),
        'email_address': forms.EmailInput(attrs={'class': 'form-control', 'Placeholder': 'Email'})
        
    }