from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from account.models import UserDetails
from django.contrib.auth import authenticate
import uuid

def home(request):
    return render(request,'homepage.html') 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psd']
        if User.objects.filter(username = username).exists():
            user = authenticate(username = username, password = password)
            UserDetails.objects.filter(user=user).update(auth_token=uuid.uuid4())
            if user is not None:
                messages.success(request, 'You are now logged in')
                user=User.objects.get(username = username)
                name = str(user.username)
                return redirect('dashboard',name)
            messages.error(request,'Please enter correct email and password..!')
            return redirect('login')
        messages.error(request,'That email is not registered')
        return redirect('signup')
    return render(request,'login.html')
    

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user_name = request.POST['user_name']
        phone = request.POST['phonenumber']
        address = request.POST['address']
        password = request.POST['pds']
        confirm_password = request.POST['Cpds']
        if password == confirm_password:
            if not User.objects.filter(username = user_name ).exists():
                user = User.objects.create_user(password = password, email = email, first_name = first_name, last_name = last_name, username = user_name )
                UserDetails.objects.create(user=user,address=address,phone=phone,auth_token=uuid.uuid4())
                messages.success(request, 'You can now logged in')
                return redirect('login')
            messages.error(request,'Sorry, this user is already in used..!')
            return redirect('signup')
        messages.error(request,'Passwords do not match')
        return redirect('signup')
    return render(request,'signup.html') 
   

def contact(request):
    return render(request,'contact.html')  

def dashboard(request,name):
    if request.method == 'POST':
        user = User.objects.get(username=name)
        print(user.username)    
        UserDetails.objects.filter(user=user).update(auth_token=str(uuid.uuid4()))
        messages.success(request, 'You are logged out')
        return redirect('login')
    print(name)
    return render(request, 'dashboard.html')