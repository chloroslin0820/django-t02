from django.shortcuts import render

def home(req):
    return render(req, 'home.html')

def login(req):
    return render(req, 'login.html')

def register(req):
    return render(req, 'register.html')