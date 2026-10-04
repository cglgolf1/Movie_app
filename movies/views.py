from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'movies': ['Top Gun', 'gladiator', 'babe'],
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

