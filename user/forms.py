from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': "text", 'class': 'w-100 form-control border-0 py-3 mb-4', 'placeholder': "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'type': "email", 'class': 'w-100 form-control border-0 py-3 mb-4', 'placeholder': 'Enter Your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'type': "password", 'class': 'w-100 form-control border-0 py-3 mb-4', 'placeholder': 'Password'}),
        label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'type': "password", 'class': 'w-100 form-control border-0 py-3 mb-4',
               'placeholder': 'Confirm Password'}), label='Confirm Password')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-100 form-control border-0 py-3 mb-4',
            'placeholder': 'Enter Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-100 form-control border-0 py-3 mb-4',
            'placeholder': 'Enter Password'
        })
    )
