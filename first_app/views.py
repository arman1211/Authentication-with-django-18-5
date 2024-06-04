from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created succesfully')
            print(form.cleaned_data)
            return redirect('home')
    else:

        form = forms.RegisterForm()
    return render(request, 'register.html',{'form': form})

def loginuser(request):
    if request.method == 'POST':
        form = forms.LoginUser(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username,password)
            user = authenticate(request, username= username, password = password)
            print(user)
            if user is not None:

                login(request,user)
                messages.success(request,'Logged in succesfull')
                return redirect('profile')
            else:
                messages.warning(request,'Invalid username or password')
    else:
        form = forms.LoginUser()
    return render(request,'register.html',{'form': form})

@login_required
def logoutuser(request):
    logout(request)
    messages.success(request,'Logged out succesfully')
    return redirect('home')

@login_required
def profileuser(request):
    return render(request, 'profile.html')