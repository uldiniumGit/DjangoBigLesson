from django.contrib import admin
from .models import City, Type, Client, News

# Register your models here.

admin.site.register(City)
admin.site.register(Type)
admin.site.register(Client)
admin.site.register(News)
