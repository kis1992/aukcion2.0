from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import BaseUser


class SignUpForm(UserCreationForm):    
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    phone_number = forms.CharField(required=True, max_length=30, label=("phone"))
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=("Password(again)"))
    email = forms.EmailField(label=("E-mail"), widget=forms.EmailInput,)

    class Meta:
        model = BaseUser
        fields = ('username', 'email', 'birth_date', 'phone_number', 'password1', 'password2',)
