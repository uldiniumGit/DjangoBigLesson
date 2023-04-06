from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('prices/', views.Prices.as_view(), name='prices'),
    path('client_list/', views.ClientsListView.as_view(), name='client_list'),
    path('delivery/', views.Delivery.as_view(), name='delivery'),
    path('buy/', views.Buy.as_view(), name='buy'),
    path('check/', views.Check.as_view(), name='check'),
    path('export/', views.Export.as_view(), name='export'),
    path('contact_us/', views.ContactUs.as_view(), name='contact_us'),
    path('submit_application/', views.Application.as_view(), name='submit_application'),
    path('news01/', views.News01.as_view(), name='news01'),
    path('news02/', views.News02.as_view(), name='news02'),
    path('news03/', views.News03.as_view(), name='news03'),
    path('news-list/', views.NewsListView.as_view(), name='news_list'),
    path('create_news/', views.CreateNews.as_view(), name='create_news')
]

