from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView

from .models import Client, News
from django.views.generic.base import ContextMixin


'''
в каждой вьюшке происходит проверка на кол-во новостей, в зависимости от этого
рендерится страница
'''


# Главная страница
def main_view(request):
    client = Client.objects.all()
    news = News.objects.order_by('-id')
    if len(news) == 0:
        return render(request, 'test_app/index.html', context={'client': client})
    if len(news) == 1:
        news00 = news[0]
        return render(request, 'test_app/index.html', context={'client': client, 'news00': news00})
    elif len(news) == 2:
        news00 = news[0]
        news01 = news[1]
        return render(request, 'test_app/index.html', context={'client': client, 'news00': news00, 'news01': news01})
    elif len(news) >= 3:
        news00 = news[0]
        news01 = news[1]
        news02 = news[2]
        return render(request, 'test_app/index.html',
                      context={'client': client, 'news00': news00, 'news01': news01, 'news02': news02})


# Класс для множественного наследования.
# Добавляем контекст для всех страниц.
class NewsContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        """
        context = super().get_context_data(**kwargs)
        news = News.objects.order_by('-id')
        if len(news) == 0:
            return context
        elif len(news) == 1:
            news00 = news[0]
            context['news00'] = news00
            return context
        elif len(news) == 2:
            news00 = news[0]
            context['news00'] = news00
            news01 = news[1]
            context['news01'] = news01
            return context
        elif len(news) >= 3:
            news00 = news[0]
            context['news00'] = news00
            news01 = news[1]
            context['news01'] = news01
            news02 = news[2]
            context['news02'] = news02
            return context


# Цены
class Prices(TemplateView, NewsContextMixin):
    template_name = 'test_app/prices.html'


# Наши услуги. 4 вкладки
class Delivery(TemplateView, NewsContextMixin):
    template_name = 'test_app/delivery.html'


class Buy(TemplateView, NewsContextMixin):
    template_name = 'test_app/buy.html'


class Check(TemplateView, NewsContextMixin):
    template_name = 'test_app/check.html'


class Export(TemplateView, NewsContextMixin):
    template_name = 'test_app/export.html'


class Application(CreateView, NewsContextMixin):
    fields = ['name', 'description', 'email']
    model = Client
    success_url = reverse_lazy('test_app:index')
    template_name = 'test_app/submit_application.html'


'''
!!!!!!
'''


class CreateNews(CreateView, NewsContextMixin):
    fields = ['title', 'text', 'video_link']
    model = News
    success_url = reverse_lazy('test_app:news01')
    template_name = 'test_app/create_news.html'


class ContactUs(TemplateView, NewsContextMixin):
    template_name = 'test_app/contact_us.html'


'''
!!!!!!!!!!!!!!!!!! Блок с новостями !!!!!!!!!!!!!!!!!!
'''


class News01(TemplateView, NewsContextMixin):
    template_name = 'test_app/news_01.html'


class News02(TemplateView, NewsContextMixin):
    template_name = 'test_app/news_02.html'


class News03(TemplateView, NewsContextMixin):
    template_name = 'test_app/news_03.html'


class NewsListView(ListView, NewsContextMixin):
    model = News
    template_name = 'test_app/news_list.html'

    def get_queryset(self):
        return super(NewsListView, self).get_queryset().order_by('-id')


class ClientsListView(ListView, NewsContextMixin):
    model = Client
    template_name = 'client_list.html'


# DONE создать четыре страницы под последние новости. Страница должна наполняться данными из списка новостей.
# DONE создать страницу со списком всех старых новостей
# DONE красиво оформить страницу новостей
# DONE убрать из проекта приложение для видео
# Done сделать проверку существует ли три новости, чтобы сайт не падал при отсутствии новостей
# DONE сделать новую форму для новостей
# DONE поменять проверку, чтобы она могла показывать не только по 0 или 3 новости
# TODO добавить регистрацию
# TODO перенести добавление новостей в админку
# TODO сделать адаптивный дизайн
