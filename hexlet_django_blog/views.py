from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def index(request):
    return redirect('article', kwargs={'article_id': 42, 'tags': 'python'})

# для страницы about
def about(request):
    return render(request, 'about.html')