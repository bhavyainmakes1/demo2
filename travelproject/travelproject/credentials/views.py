from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
def register(request):
    if (request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        password1= request.POST['password1']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name= request.POST['last_name']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('credentials:user_login')
        else:
            messages.info(request,'Passwords are not matching')
            return redirect('credentials:register')



    return render(request,'register.html')
def user_login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid login details")
            return redirect('user_login')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return user_login(request)