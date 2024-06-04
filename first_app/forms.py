from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

# class LoginUser(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = '__all__'

class LoginUser(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )



