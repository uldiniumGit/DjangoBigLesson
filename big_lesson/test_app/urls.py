from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('pricing/', views.show_prices, name='pricing'),
    path('about/', views.about, name='about'),
]
