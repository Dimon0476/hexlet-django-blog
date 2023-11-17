"""
URL configuration for hexlet_django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog import views

urlpatterns = [
    path('', views.index), # <- обработка адреса главной страницы
    path('articles/', include('hexlet_django_blog.article.urls')),  # <- новая строчка для article.
                                            # С этого момента все пути, которые начинаются с "articles/",
                                            # будут перенаправляться в hexlet_django_blog.article.urls.
                                            # В приложении у нас уже приписана view index, которая связана с путем ''.
                                            # Это означает, что запрос по пути articles/ без каких либо продолжений
                                            # будет направлен в hexlet_django_blog.article.views.index.
    path('about/', views.about), # <- добавляем эту строчку для страницы about/
    path('admin/', admin.site.urls),
]
