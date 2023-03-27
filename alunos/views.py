from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def alunos(request):

    return render(request, 'notas.html')


