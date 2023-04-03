from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    type = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.type


class Client(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    email = models.EmailField(max_length=32, unique=True)

    # Связь с категорией
    # Один - много
    # email = models.ForeignKey(Email, on_delete=models.CASCADE)

    # Много - много
    # city = models.ManyToManyField(City, null=True, blank=True)

    # type = models.ManyToManyField(Type, null=True, blank=True)

    # Картинка
    # image = models.ImageField(upload_to='clients', null=True, blank=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True)
    text = models.TextField(null=True)
    video_link = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title
