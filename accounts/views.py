from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from listings.models import Listing


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # User Autentification
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    # Login Get Requests
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # User Verification
        if not User.objects.filter(username=username).exists():
            # Email Verification
            if not User.objects.filter(username=username).exists():
                # Password Verification
                if password == password2:
                    # Create and Save the new user in the BD
                    new_user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                        username=username, email=email, password=password)
                    new_user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')

                # Password Error
                else:
                    messages.error(request, 'Passwords do not match')
                    return redirect('register')
            # Email Error
            else:
                messages.error(request, 'That email is being used')
                return redirect('register')
        # Username Error
        else:
            messages.error(request, 'That username is taken')
            return redirect('register')

    # Register GET requests
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Now you are log out')
    return redirect('index')


def dashboard(request):
    listings = Listing.objects.order_by('-list_date')
    context = {
        listings: 'listings'
    }
    return render(request, 'accounts/dashboard.html', context)
