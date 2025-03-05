from django.http import HttpResponse
from lib2to3.fixes.fix_input import context

from django.shortcuts import render


menu = [{'title': "О себе", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'addpage'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
        ]

category = [{'title': "Для родителей", 'url_name': 'parent'},
        {'title': "Достижения воспитанников", 'url_name': 'progress'},
        {'title': "Нормативно-правовые документы", 'url_name': 'ntd'},
        ]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]



def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'category': category,
    }
    return render(request, 'garten/index.html', context=data)


def about(request):
    return render(request, 'garten/about.html', {'title': 'О себе', 'menu': menu, 'category': category})


def addpage(request):
    return HttpResponse('Добавить статью')

def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def parent(request):
    # return HttpResponse('Для родителей')
    return render(request, 'garten/parent.html', {'title': 'О сайте', 'menu': menu, 'category': category})


def progress(request):
    return render(request, 'garten/progress.html', {'title': 'О сайте', 'menu': menu, 'category': category, 'title2': 'Достижения воспитанников'})

def ntd(request):
    return render(request, 'garten/ntd.html', {'title': 'О сайте', 'menu': menu, 'category': category})
