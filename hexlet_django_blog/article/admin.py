from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

# Register your models here.
from .models import Article

@admin.register(Article) # позволяет связать модель с классом и провести регистрацию модели в разделе администратора вместо строки: admin.site.register(Article, ArticleAdmin)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp') # Перечисляем поля, отображаемые в таблице списка статей
    search_fields = ['name', 'body']
    list_filter = (('timestamp', DateFieldListFilter),) # Перечисляем поля для фильтрации


# admin.site.register(Article, ArticleAdmin)