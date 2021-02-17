from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import User, Blog
from .forms import UserForm, BlogForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            user1=user.save()
            user1.set_password(user1.password)
            user1.save()
            user = UserForm()
            return redirect('login')
    else:
        user = UserForm()
    return render(request,'register.html', {'user':user})



def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                print("\n In LOGIN \n")
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user != None:
                    login(request, user)
                    return render(request,'test.html')
                else:
                    print("Someone tried to login and failed.")
                    print("They used username: {} and password: {}".format(username,password))
                    return render(request,  "registration/login.html")
        else:
            form = AuthenticationForm()
        return render(request,'registration/login.html',{'form':form})
    else:       
        return render(request, 'registration/login.html')



def logout_view(request):
    logout(request)
    return redirect('index')


def test(request):
    return render(request,'test.html')



