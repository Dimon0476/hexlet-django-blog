from django.shortcuts import render
from django.shortcuts import redirect, reverse

# Create your views here.
from django.http import HttpResponse


def index(request, tags=None, article_id=None):
    article_id = 42
    tags = 'python'

    return render(request, 'articles/index.html', context={'article_id': article_id, 'tags': tags})
    # return redirect('article')
