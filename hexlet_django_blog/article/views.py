from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    tags = ['Articles', 'статьи', 'набор статей', 'python', 'oop']
    return render(
        request,
        'articles/index.html',
        context={'tags': tags},
    )