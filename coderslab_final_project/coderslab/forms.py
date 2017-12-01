from django import forms
from .models import PRIORITY
# from django.forms import Form, ModelForm
# from django.contrib.auth.models import User


class UserCreateForm(forms.Form):
    username = forms.CharField(label="Nazwa uzytkownika", max_length=100)
    password = forms.CharField(label="Haslo", max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtorz haslo", max_length=100, widget=forms.PasswordInput)
    first_name = forms.CharField(label="Imie", max_length=100)
    last_name = forms.CharField(label="Nazwisko", max_length=100)
    email = forms.CharField(label="e-mail", max_length=100, widget=forms.EmailInput)

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get


class UserAuthenticateForm(forms.Form):
    user = forms.CharField(label="User", max_length=100)
    password = forms.CharField(label="password", widget=forms.PasswordInput, max_length=100)


class AddListForm(forms.Form):
    title = forms.CharField(max_length=255)


class AddItemToListForm(forms.Form):
    title = forms.CharField(max_length=255)
    priority = forms.ChoiceField(PRIORITY)
    completed = forms.BooleanField()