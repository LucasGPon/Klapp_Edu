from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def home(request):

    return render(request, 'home.html')


def login(request):

    return render(request, 'login.html')

def cadastro(request):
   
    return render(request, 'cadastro.html')
