from django.db import models
from django.contrib.auth.models import AbstractUser


class DeliveryUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_news_maker = models.BooleanField(default=False)

