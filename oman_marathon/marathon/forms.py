from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ContactUsMessage
from django.contrib.auth.models import User
from .models import Runner

class RunnerUpdateForm(forms.ModelForm):
    class Meta:
        model = Runner
        fields = ['biography', 'healthy_condition', 'nationality', 'chosen_run']


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }


class RunnerLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RunnerCreationForm(forms.ModelForm):
    class Meta:
        model = Runner
        fields = ['biography', 'healthy_condition', 'nationality', 'chosen_run']

