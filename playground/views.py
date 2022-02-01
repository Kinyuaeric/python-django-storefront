from atexit import register
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.template import context
from . models import Feature

# Create your views here.
def say_index(request):
    features = Feature.objects.all()

    
    return render(request,'index.html',{'features':features})


def say_register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already in used")
                return redirect('register')
            elif User.objects.filter(usermame=username).exists():
                messages.info(request,"Username already in use")
                return redirect('register')
            else:
                usermame = User.object.create_user(username=username,email=email,password=password)
                usermame.save();
                return redirect('login') 
            
        else:
            messages.info(request,"Password not the same")
            return redirect('register')
         
        
    return render(request, 'register.html')

def say_login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'check credentials')
            return redirect('login')
    else:
        
        return render(request, 'login.html')
    

def say_counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words}) 
