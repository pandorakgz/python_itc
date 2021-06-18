from django.shortcuts import render
from datetime import datetime
from blog.wallet import wallet
from .models import Todo
# from .db import mydb

# Create your views here.


def home(request):
    title = 'Главная страница'
    return render(request, 'home.html', {
        'title': title
    })


def about(request):
    title = 'Страница О нас'
    return render(request, 'about.html', {
        'title': title
    })


def time(request):
    title = 'Страница показа времени'
    time_now = datetime.now()
    return render(request, 'time.html', {
        'time_now': time_now,
        'title': title
    })


def mywallet(request):
    return render(request, 'mywallet.html', {
        'wallet': wallet
    })


def todo(request):
    # cur = mydb.cusor()
    # todos_list = cur.execute('''
    #     SELECT * FROM todos
    # ''')
    # todos_all = todos_list.fetchall()
    # print(todos_all)

    todos_list = Todo.objects.all()
    return render(request, 'todo.html', {
        'todos': todos_list
    })