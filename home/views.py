from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def home(request):

    return render(request, 'home.html')

def SobreNois(request):
    return render (request, 'SobreNois.html')
