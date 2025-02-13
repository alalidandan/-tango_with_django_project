from django.shortcuts import render
from django.conf import settings

# Create your views here.
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'Dana'}
    return render(request, 'rango/about.html', context=context_dict)

