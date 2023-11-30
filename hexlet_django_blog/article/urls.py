from django.urls import path

from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleCommentsView, ArticleFormCreateView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view()),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]