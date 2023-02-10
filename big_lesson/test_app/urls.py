from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
    path('', views.main_view),
    path('pricing', views.show_prices),
    path('about', views.about),
]
