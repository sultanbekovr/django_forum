from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    first_name = forms.CharField(label='Ваше имя', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))