from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from webapp.models import TestPassword
import logging

logger = logging.getLogger("swindle")


def index(request):
    return render(request, 'index.html', {})

@login_required(login_url="/webapp/")
def dashboard(request):
    user = request.user
    data = {
        "username": user.username,
        "email": user.email,
    }
    return render(request, 'dashboard.html', data)

def register(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    
    try:
        user = User.objects.create_user(username, email, password)
    except IntegrityError:
        logger.error("Could not create user : username=%s, email=%s" % (username, email))
        messages.error(request, 'Could not create user account.')
        return HttpResponseRedirect("/webapp")
    user.first_name=first_name
    user.last_name=last_name
    user.save()
    test_password = TestPassword(user=user, test_password=password)
    test_password.save()

    user = authenticate(username=username, password=password)
    _login(request, user)
    messages.success(request, 'Account created.')
    return HttpResponseRedirect("/webapp/dashboard")

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
