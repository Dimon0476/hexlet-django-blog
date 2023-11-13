from django.shortcuts import render

# Здесь мы используем функцию render.
# Она формирует HTML на основе указанного шаблона и
# использует при рендеринге (составлении страницы) данные из словаря context.
# index.html:
def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })

# для страницы about
def about(request):
    return render(request, 'about.html')