Учебный проект "Новости Info to Go"
Урок 1
Создали проект itg
Создали репозиторий
Создали проект itg
Установили зависимости pip install django
Сохранили зависимости в файл requirements.txt командой pip freeze > requirements.txt
Развернуть проект на локальной машине через командную строку:

Склонировать репозиторий
Перейти в папку проекта
Создать виртуальное окружение python -m venv venv
Активировать виртуальное окружение source venv/bin/activate на Linux/MacOS или .\venv\Scripts\activate.bat на Windows
Установить зависимости pip install -r requirements.txt
Либо через PyCharm:

Склонировать репозиторий через File -> Project from Version Control
Установить зависимости через File -> Settings -> Project Interpreter или через pip install -r requirements.txt
Создание Django project
Создать проект django-admin startproject itg . Этой командой мы создадим проект с именем itg в текущей директории. Точка в конце команды означает, что проект будет создан в текущей директории, без создания дополнительной директории с именем проекта.

commit: Урок 1: создаём django проект

Запуск проекта python manage.py runserver Для запуска проекта, вам нужно использовать терминал, и находясь в директории проекта, на одном уровне с файлом manage.py, выполнить команду python manage.py runserver Для остановки сервера используйте комбинацию клавиш Ctrl+C

Команды терминала:

python manage.py runserver - запуск сервера
cd - смена директории
cd.. - переход на уровень выше
ls - просмотр содержимого директории
pwd - показать текущую директорию
commit: Урок 1: запускаем django сервер

Создание приложения python manage.py startapp news После создания приложения, вам нужно зарегистрировать его в файле settings.py в разделе INSTALLED_APPS

commit: Урок 1: cоздаём django_app news

Создали первое представление
from django.http import HttpResponse
def main(request):
    return HttpResponse("Hello, world!")  # вернет страничку с надписью "Hello, world!"
Чтобы представление заработало, его нужно зарегистрировать в файле urls.py конфигурации проекта.

Создали первый URL
from news import views
path('', views.main),
Теперь, если вы перейдете на главную страницу сайта, то увидите надпись "Hello, world!"

commit: Урок 1: создаём первый маршрут и первое представление

Урок 2
Создаем детальное представление новости по ее ID
Для этого нам нужно создать новый маршрут, с конвертером int, который будет принимать ID новости.

path('news/<int:news_id>/', views.news_detail),
А так же функцию, которая будет обрабатывать запрос и возвращать страницу с детальной информацией о новости.

def news_by_id(request, news_id):
    return HttpResponse(f"Новость с ID {news_id}")
include и собственный файл urls.py для приложения news
Создали еще одно представление get_all_news в файле views.py
Создали файл urls.py в директории приложения news
Зарегистрировали новый файл urls.py в файле urls.py конфигурации проекта с помощью функции include
Зарегистрировали маршруты без префикса news/ в файле urls.py приложения news
commit: Урок 2: собственный urls.py в news и функция include

Знакомство с Django Templates (Шаблоны)
Создали папку templates в директории приложения news
Создали файл catalog.html в директории templates/news
Переписали функцию get_all_news в файле views.py так, чтобы она возвращала страницу catalog.html используя функцию render из модуля django.shortcuts
commit: Урок 2: рендер первого шаблона

Работа с шаблоном
Создали словарь с данными в views.py и передали его в шаблон
info = {
    "users_count": 100600,
    "news_count": 1000,
}
Вставили данные в шаблон catalog.html с помощью шаблонного языка Django Template Language (DTL)

Подключили BS5 по CDN и стилизовали страницу

*commit: Урок 2: передаём первые данные в шаблон и подключил BS5

Смотрим типы данных внутри шаблона
Проверили, что можно передать только словарь
Передали список и вывели его в шаблоне
Передали список меню и познакомились с конструкцией {% for item in menu %}
Познакомились с конструкцией {% comment %} {% endcomment %} для комментирования участков шаблона
commit: Урок 2: первый цикл в шаблоне

Посмотрели на тег шаблона if
Сделали <hr> после каждого элемента списка, кроме последнего с помощью специальной переменной forloop.last

commit: Урок 2: первый тег if в шаблоне

Сделали ссылки в меню кликабельными
Передали в шаблон список словарей, где каждый словарь содержит url и title
commit: Урок 2: сделали ссылки в меню кликабельными

Описали маршруты /catalog, /catalog/<int:news_id/>, /catalog/<slug:slug> и создали соответствующие представления в файле views.py
catalog возвращает HttpResponse("Каталог новостей")
get_news_by_id возвращает HttpResponse(f"Новость {news_id}")
get_category_by_name возвращает HttpResponse(f"Карточка {slug}")
commit: Урок 2: добавили новые маршруты