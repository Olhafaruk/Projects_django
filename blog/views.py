from django.http import HttpResponse
from django.shortcuts import render

info = {
    "users_count": 100600,
    "blog_count": 100600,
    "menu": [
        {"title": "Главная", "url": "/", "url_name": "index"},
        {"title": "О проекте", "url": "/about/", "url_name": "about"},
        {"title": "Каталог", "url": "/blog/catalog/", "url_name": "catalog"},
    ]
}


def main(request):
    return HttpResponse("Hello, world") # Вернёт страницу с надписью "Hello world!"

def about(request):
    return HttpResponse("information page")

def catalog(request):
    return HttpResponse("Каталог новостей")

def get_category_by_name(request, slug):
    return HttpResponse(f"Категория {slug}")

def get_all_blog(request):
    return render(request, "blog/catalog.html", context=info)

def get_blog_by_id(request, blog_id):
    if blog_id > 10:
        return HttpResponse("Такой новости нет", status=404)
    return HttpResponse(f'Вы открыли новость {blog_id}')  # Вернёт страницу с надписью "Вы открыли новость {blog_id}"

# Create your views here.
