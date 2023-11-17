from django.apps import AppConfig


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hexlet_django_blog.article'  # <- изменяем эту строчку.
                                        # Чтобы закончить создание болванки приложения,
                                        # остается задать его имя в файле apps.py и
                                        # подключить в settings.INSTALLED_APPS.
                                        # Для этого в качестве имени мы указываем полный путь к приложению
