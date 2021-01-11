from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import BaseUser


class SignUpForm(forms.Form):    
    date_of_birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    phone_number = forms.CharField(required=True, max_length=30, label=("phone"),help_text='Required. Format: +7 (7778885511)')
    username = forms.CharField(required=True, label=("username"))
    email = forms.EmailField(label=("E-mail"), widget=forms.EmailInput,)
    photo = forms.FileField(label=("Avatar"))


    class Meta:
        model = BaseUser
        fields = ('username', 'email', 'date_of_birth', 'phone_number','photo')
