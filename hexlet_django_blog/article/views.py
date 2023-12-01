from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm


class IndexView(ListView):
    model = Article
    template_name = 'articles/index.html'


class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/create.html'


class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/update.html'


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:index')
    template_name = 'articles/delete.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'articles/detail.html'
