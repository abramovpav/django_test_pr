from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.

def login(request):
    message = None
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    if password and username:
        user = authenticate(username=str(username), password=str(password))
        if user is not None:
            # the password verified for the user
            if user.is_active:
                print("User is valid, active and authenticated")
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            message = "The username and/or password were incorrect."
    return render(request, 'authentication/login.html', context={'message': message})
