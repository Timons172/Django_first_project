import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time().replace(microsecond=0)
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    directory = os.getcwd()
    content = os.listdir(directory)
    response_content = f"Текущая директория: {directory}\n"
    response_content += "\n".join(content)
    return HttpResponse(response_content, content_type="text/plain; charset=utf-8")
