from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Client, News
from .forms import ContactForm
from django.core.mail import send_mail


# Главная страница
def main_view(request):
    client = Client.objects.all()
    return render(request, 'test_app/index.html', context={'client': client})


# Цены
def show_prices(request):
    return render(request, 'test_app/pricing.html')


# Наши услуги. 4 вкладки
def delivery_to_rf(request):
    return render(request, 'test_app/DeliveryToRF.html')


def redemption_of_goods(request):
    return render(request, 'test_app/RedemptionOfGoods.html')


def goods_check(request):
    return render(request, 'test_app/GoodsCheck.html')


def export_of_personal_belongings(request):
    return render(request, 'test_app/ExportOfPersonalBelongings.html')


# TODO страница пока не используется
# О нас
def about(request):
    return render(request, 'test_app/about.html')


# Оставить заявку
def application(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            # TODO пока не работает 1
            a = Client()
            a.name = name
            a.email = email
            a.description = message

            send_mail(
                'contact',
                f'{name}, ваше сообщение {message} принято',
                'uldinium@yandex.ru',
                [email],
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('test_app:index'))
        else:
            return render(request, 'test_app/application.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'test_app/application.html', context={'form': form})


#  Новости
def news(request):
    our_news = News.objects.all()
    return render(request, 'test_app/news.html', context={'our_news': our_news})


# Контакты
def contact(request):
    return render(request, 'test_app/contact.html')
