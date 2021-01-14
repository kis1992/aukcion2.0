from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import BaseUser
from django.contrib.auth.base_user import BaseUserManager


class SignUpForm(forms.Form):
    username = forms.CharField(required=True, label=("username"))
    email = forms.EmailField(label=("E-mail"), widget=forms.EmailInput,required=True)
    phone_number = forms.CharField(required=True, max_length=30, label=("phone"),help_text='Required. Format: +7 (7778885511)')
    date_of_birth = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    photo = forms.FileField(label=("Avatar"))


    class Meta:
        model = BaseUser
        fields = ('username', 'email', 'date_of_birth', 'phone_number','photo')

    """def __int__(self):
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'"""

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        clean_email = self.cleaned_data["email"]
        clean_password = BaseUserManager().make_random_password()
        user.set_password(clean_password)
        user.email = clean_email
        user.save()
        return user