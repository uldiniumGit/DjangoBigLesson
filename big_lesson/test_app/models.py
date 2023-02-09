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
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=32, unique=True)

    # Связь с категорией
    # Один - много
    # email = models.ForeignKey(Email, on_delete=models.CASCADE)

    # Много - много
    city = models.ManyToManyField(City)

    type = models.ManyToManyField(Type)

    def __str__(self):
        return self.name

