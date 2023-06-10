from django.contrib import admin
from .models import Client, News, Feedback, Imgs

# Register your models here.

admin.site.register(Client)
admin.site.register(News)
admin.site.register(Feedback)
admin.site.register(Imgs)
