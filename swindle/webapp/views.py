from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.contrib.auth.decorators import login_required
from webapp.models import UserManager
import logging

logger = logging.getLogger("swindle")


def index(request):
    return render(request, 'index.html', {})

@login_required(login_url="/webapp/")
def dashboard(request):
    user = request.user
    data = {
        "user": user,
    }
    return render(request, 'dashboard.html', data)

def register(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    
    manager = UserManager()
    if manager.create_user(first_name, last_name, username, email, password):
        user = authenticate(username=username, password=password)
        _login(request, user)
        messages.success(request, 'Account created.')
        return HttpResponseRedirect("/webapp/dashboard")
    else:
        messages.error(request, 'Could not create user account.')
        return HttpResponseRedirect("/webapp")


def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is None:
        messages.error(request, 'Bad credentials.')
        return HttpResponseRedirect("/webapp")
    _login(request, user)
    return HttpResponseRedirect("/webapp/dashboard")

def logout(request):
    _logout(request)
    return HttpResponseRedirect("/webapp")
