from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views.generic.base import ContextMixin

from .models import Client, News, Feedback, Imgs

'''
В каждой вьюшке происходит проверка на кол-во новостей, в зависимости от этого
рендерится страница
'''

# Главная страница
def main_view(request):
    feedback = Feedback.objects.all()
    news = News.objects.order_by('-id')
    photos = Imgs.objects.order_by('-id')
    photos00 = photos[0] if photos.exists() else None

    news_list = list(news[:3])  # получаем максимум 3 новости

    context = {'feedback': feedback, 'photos00': photos00}

    if len(news_list) >= 1:
        context['news00'] = news_list[0]
    if len(news_list) >= 2:
        context['news01'] = news_list[1]
    if len(news_list) >= 3:
        context['news02'] = news_list[2]

    return render(request, 'test_app/index.html', context)


# Класс для множественного наследования.
# Добавляем контекст для всех страниц.
class NewsContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        """
        context = super().get_context_data(**kwargs)
        news = list(News.objects.order_by('-id')[:3])
        if len(news) >= 1:
            context['news00'] = news[0]
        if len(news) >= 2:
            context['news01'] = news[1]
        if len(news) >= 3:
            context['news02'] = news[2]
        return context


# Цены
class Prices(NewsContextMixin, TemplateView):
    template_name = 'test_app/prices.html'


# Наши услуги. 4 вкладки
class Delivery(NewsContextMixin, TemplateView):
    template_name = 'test_app/delivery.html'


class Buy(NewsContextMixin, TemplateView):
    template_name = 'test_app/buy.html'


class Check(NewsContextMixin, TemplateView):
    template_name = 'test_app/check.html'


class Export(NewsContextMixin, TemplateView):
    template_name = 'test_app/export.html'


class Application(NewsContextMixin, CreateView):
    fields = ['description', 'link', 'color', 'amount', 'price', 'name', 'phone_number']
    model = Client
    success_url = reverse_lazy('test_app:index')
    template_name = 'test_app/submit_application.html'


# TODO  1
class CreateFeedback(UserPassesTestMixin, NewsContextMixin, CreateView):
    fields = ['name', 'link', 'img']
    model = Feedback
    success_url = reverse_lazy('test_app:index')
    template_name = 'test_app/create_feedback.html'

    def test_func(self):
        return self.request.user.is_superuser


class Photos(UserPassesTestMixin, NewsContextMixin, CreateView):
    fields = ['name', 'img1', 'img2', 'img3']
    model = Imgs
    success_url = reverse_lazy('test_app:index')
    template_name = 'test_app/photos.html'

    def test_func(self):
        return self.request.user.is_superuser


class CreateNews(UserPassesTestMixin, NewsContextMixin, CreateView):
    fields = ['title', 'video_link', 'text', 'img1', 'img2', 'img3', 'img4', 'img5']
    model = News
    success_url = reverse_lazy('test_app:news01')
    template_name = 'test_app/create_news.html'

    def test_func(self):
        return self.request.user.is_superuser


# Регистрация сигнала в этом же файле, вне класса, чтобы он точно сработал
@receiver(pre_save, sender=News)
def change_video_link(sender, instance, **kwargs):
    if not instance.video_link:
        return
    video_link = instance.video_link.replace("watch?v=", "embed/")
    try:
        index = video_link.index("&")
        video_link = video_link[:index]
    except ValueError:
        pass
    instance.video_link = video_link


class ContactUs(NewsContextMixin, TemplateView):
    template_name = 'test_app/contact_us.html'


'''
Блок с новостями
'''


class News01(NewsContextMixin, TemplateView):
    template_name = 'test_app/news_01.html'


class News02(NewsContextMixin, TemplateView):
    template_name = 'test_app/news_02.html'


class News03(NewsContextMixin, TemplateView):
    template_name = 'test_app/news_03.html'


class NewsListView(NewsContextMixin, ListView):
    model = News
    template_name = 'test_app/news_list.html'
    paginate_by = 2
    title = 'Новости'

    def get_queryset(self):
        return super().get_queryset().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class ClientsListView(UserPassesTestMixin, NewsContextMixin, ListView):
    model = Client
    template_name = 'test_app/client_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('-id')

    def test_func(self):
        return self.request.user.is_superuser


class ClientDeleteView(NewsContextMixin, DeleteView):
    template_name = 'test_app/client_delete_confirm.html'
    model = Client
    success_url = reverse_lazy('test_app:client_list')


class NewsDeleteView(NewsContextMixin, DeleteView):
    template_name = 'test_app/news_delete_confirm.html'
    model = News
    success_url = reverse_lazy('test_app:news_list')


class NewsUpdateView(NewsContextMixin, UpdateView):
    fields = ['title', 'video_link', 'text', 'img1', 'img2', 'img3', 'img4', 'img5']
    model = News
    success_url = reverse_lazy('test_app:news_list')
    template_name = 'test_app/create_news.html'
