from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Import  models
from .models import Feature


# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

# route to register.html page
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Password and Email VAlidation
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Registered')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Passwords not match') 
            return redirect('register') 
    else:    
        return render(request, 'register.html')

def counter(request):
    text = request.POST['text'] 
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})