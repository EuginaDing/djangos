from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from travello.models import Course

# Create your views here.
def register(request):
    if request.method=='POST':
        usernameR=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=usernameR).exists():
                messages.info(request,'you already in!' )
                return redirect('register')
            else:
                user=User.objects.create_user(username=usernameR, password=password1, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password not match!" )
            return redirect('register')
    return render(request, 'register.html')

def login(request):
   if request.method=='POST':
        usernameR=request.POST['username']
        password=request.POST['password'] 
        #if User.objects.filter(username=usernameR, password=password).exists():
        user=auth.authenticate(username=usernameR, password=password)
        if user:
            auth.login(request, user)
            return redirect('oneschoolHome')
        
        else:
            messages.info(request,"password wrong")
            return redirect('login')
   return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def oneschoolHome(request):
 
    dests=Course.objects.all()
   # print(dest.username for dest in dests)
    return render(request, "oneschoolHome.html", {"dests": dests})