from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Client, News
from .forms import ContactForm
from django.core.mail import send_mail


# Главная страница
def main_view(request):
    client = Client.objects.all()
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/index.html', context={'client': client, 'news00': news00, 'news01': news01, 'news02': news02})


# Цены
def show_prices(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/pricing.html', context={'news00': news00, 'news01': news01, 'news02': news02})


# Наши услуги. 4 вкладки
def delivery_to_rf(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/DeliveryToRF.html', context={'news00': news00, 'news01': news01, 'news02': news02})


def redemption_of_goods(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/RedemptionOfGoods.html', context={'news00': news00, 'news01': news01, 'news02': news02})


def goods_check(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/GoodsCheck.html', context={'news00': news00, 'news01': news01, 'news02': news02})


def export_of_personal_belongings(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/ExportOfPersonalBelongings.html', context={'news00': news00, 'news01': news01, 'news02': news02})


# TODO страница пока не используется
# О нас
def about(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/about.html', context={'news00': news00, 'news01': news01, 'news02': news02})


# Оставить заявку
def application(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            # TODO пока не работает
            a = Client()
            a.name = name
            a.email = email
            a.description = message

            a.save()

            send_mail(
                'contact',
                f'{name}, ваше сообщение {message} принято',
                'uldinium@yandex.ru',
                [email],
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('test_app:index'))
        else:
            return render(request, 'test_app/application.html', context={'form': form, 'news00': news00, 'news01': news01, 'news02': news02})
    else:
        form = ContactForm()
        return render(request, 'test_app/application.html', context={'form': form, 'news00': news00, 'news01': news01, 'news02': news02})


# TODO страница лишняя, надо убрать после того, как доделаю новую страницу со списком новостей

#  Новости
def news_list(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/news.html', context={'news00': news00, 'news01': news01, 'news02': news02})


# Контакты
def contact(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/contact.html', context={'news00': news00, 'news01': news01, 'news02': news02})


'''
!!!!!!!!!!!!!!!!!! Блок с новостями !!!!!!!!!!!!!!!!!!
'''


# Новости 1
def news1(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/news1.html', context={'news00': news00, 'news01': news01, 'news02': news02})


# Новости 2
def news2(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/news2.html', context={'news00': news00, 'news01': news01, 'news02': news02})


# Новости 3
def news3(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/news3.html', context={'news00': news00, 'news01': news01, 'news02': news02})


# Новости еще
def more_news(request):
    news = News.objects.order_by('-id')
    news00 = news[0]
    news01 = news[1]
    news02 = news[2]
    return render(request, 'test_app/moreNews.html', context={'news': news, 'news00': news00, 'news01': news01, 'news02': news02})


# TODO создать четыре страницы под последние новости. Страница должна наполняться данными из списка новостей.
# TODO создать страницу со списком всех старых новостей
# TODO красиво оформить страницу новостей
# TODO сделать переменную для новых новостей в моделях
