from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def profile(request):
    return render(request, 'profiles/profile.html', context={'user': request.user})