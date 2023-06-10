from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Client, News, Feedback, Imgs
from django.views.generic.base import ContextMixin

'''
в каждой вьюшке происходит проверка на кол-во новостей, в зависимости от этого
рендерится страница
'''


# Главная страница
def main_view(request):
    feedback = Feedback.objects.all()
    news = News.objects.order_by('-id')
    photos = Imgs.objects.order_by('-id')
    photos00 = photos[0]
    if len(news) == 0:
        return render(request, 'test_app/index.html', context={'feedback': feedback, 'photos00': photos00})
    if len(news) == 1:
        news00 = news[0]
        return render(request, 'test_app/index.html', context={'feedback': feedback, 'photos00': photos00, 'news00': news00})
    elif len(news) == 2:
        news00 = news[0]
        news01 = news[1]
        return render(request, 'test_app/index.html',
                      context={'feedback': feedback, 'photos00': photos00, 'news00': news00, 'news01': news01})
    elif len(news) >= 3:
        news00 = news[0]
        news01 = news[1]
        news02 = news[2]
        return render(request, 'test_app/index.html',
                      context={'feedback': feedback, 'photos00': photos00, 'news00': news00, 'news01': news01, 'news02': news02})


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
    fields = ['description', 'link', 'color', 'amount', 'price', 'name', 'phone_number']
    model = Client
    success_url = reverse_lazy('test_app:index')
    template_name = 'test_app/submit_application.html'


'''
!!!!!!
'''


# TODO  1
class CreateFeedback(UserPassesTestMixin, CreateView, NewsContextMixin):
    fields = ['name', 'link', 'img']
    model = Feedback
    success_url = reverse_lazy('test_app:index')
    template_name = 'test_app/create_feedback.html'

    def test_func(self):
        return self.request.user.is_superuser


class Photos(UserPassesTestMixin, CreateView, NewsContextMixin):
    fields = ['name', 'img1', 'img2', 'img3']
    model = Imgs
    success_url = reverse_lazy('test_app:index')
    template_name = 'test_app/photos.html'

    def test_func(self):
        return self.request.user.is_superuser


class CreateNews(UserPassesTestMixin, CreateView, NewsContextMixin):
    fields = ['title', 'video_link', 'text', 'img1', 'img2', 'img3', 'img4', 'img5']
    model = News
    success_url = reverse_lazy('test_app:news01')
    template_name = 'test_app/create_news.html'

    def test_func(self):
        return self.request.user.is_superuser

    @receiver(pre_save, sender=News)
    def change_video_link(sender, instance, **kwargs):
        # получить video_link из формы
        video_link = instance.video_link
        # изменить video_link по вашему усмотрению
        video_link = video_link.replace("watch?v=", "embed/")
        # найти индекс символа "&"
        try:
            index = video_link.index("&")
            # сделать срез строки до индекса
            video_link = video_link[:index]
        except ValueError:
            # если символ "&" не найден, то ничего не делать
            pass
        # сохранить измененный video_link в экземпляре модели
        instance.video_link = video_link


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


class ClientsListView(UserPassesTestMixin, ListView, NewsContextMixin):
    model = Client
    template_name = 'test_app/client_list.html'

    def get_queryset(self):
        return super(ClientsListView, self).get_queryset().order_by('-id')

    def test_func(self):
        return self.request.user.is_superuser


class ClientDeleteView(DeleteView, NewsContextMixin):
    template_name = 'test_app/client_delete_confirm.html'
    model = Client
    success_url = reverse_lazy('test_app:client_list')


class NewsDeleteView(DeleteView, NewsContextMixin):
    template_name = 'test_app/news_delete_confirm.html'
    model = News
    success_url = reverse_lazy('test_app:news_list')


class NewsUpdateView(UpdateView, NewsContextMixin):
    fields = ['title', 'video_link', 'text', 'img1', 'img2', 'img3', 'img4', 'img5']
    model = News
    success_url = reverse_lazy('test_app:news_list')
    template_name = 'test_app/create_news.html'

