from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def HomePage(request):
    return render(request,'home.html')
def SignUpPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
     
        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Registration successful! You can now login.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Registration failed: {e}')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    return render(request, 'register.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

