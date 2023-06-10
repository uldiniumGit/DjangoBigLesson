from django.db import models
from django.utils import timezone


# Create your models here.

class Client(models.Model):

    description = models.CharField(null=True, max_length=1012, verbose_name='Описание')
    link = models.CharField(max_length=1012, blank=True, null=True, verbose_name='Ссылка')
    color = models.CharField(max_length=64, unique=False, null=True, verbose_name='Цвет')
    amount = models.CharField(null=True, max_length=64, verbose_name='Кол-во')
    price = models.CharField(null=True, max_length=64, verbose_name='Цента за шт.')
    name = models.CharField(null=True, max_length=64, verbose_name='Ваше имя')
    phone_number = models.CharField(null=True, max_length=64, verbose_name='Ваш номер телефона')
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}, {self.phone_number}'


class News(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True)
    text = models.TextField(null=True)
    video_link = models.CharField(max_length=1000, blank=True, null=True)
    img1 = models.FileField(upload_to='clients', null=True, blank=True)
    img2 = models.FileField(upload_to='clients', null=True, blank=True)
    img3 = models.FileField(upload_to='clients', null=True, blank=True)
    img4 = models.FileField(upload_to='clients', null=True, blank=True)
    img5 = models.FileField(upload_to='clients', null=True, blank=True)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=32, unique=False)
    img = models.FileField(upload_to='clients', null=True, blank=True)
    link = models.CharField(max_length=32, unique=False)

    def __str__(self):
        return self.name


class Imgs(models.Model):
    name = models.CharField(max_length=32, unique=False)
    img1 = models.FileField(upload_to='clients', null=True, blank=True)
    img2 = models.FileField(upload_to='clients', null=True, blank=True)
    img3 = models.FileField(upload_to='clients', null=True, blank=True)

    def __str__(self):
        return self.name
