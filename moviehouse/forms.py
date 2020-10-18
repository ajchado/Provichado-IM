from django import forms
from .models import DvdRegistration, CustomerRegistration

class DvdForm(forms.ModelForm):

    class Meta:
        model = DvdRegistration
        fields = ('genre', 'title')

class CustomerForm(forms.ModelForm):

    class Meta:
        model = CustomerRegistration
        fields = ('firstname', 'lastname')