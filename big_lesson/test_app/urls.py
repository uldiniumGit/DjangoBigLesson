from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('pricing/', views.show_prices, name='pricing'),
    path('about/', views.about, name='about'),
    path('news/', views.news_list, name='news'),
    path('contact/', views.contact, name='contact'),
    path('DeliveryToRF/', views.delivery_to_rf, name='DeliveryToRF'),
    path('RedemptionOfGoods/', views.redemption_of_goods, name='RedemptionOfGoods'),
    path('GoodsCheck/', views.goods_check, name='GoodsCheck'),
    path('ExportOfPersonalBelongings/', views.export_of_personal_belongings, name='ExportOfPersonalBelongings'),
    path('application/', views.application, name='application'),
    path('news1/', views.news1, name='news1'),
    path('news2/', views.news2, name='news2'),
    path('news3/', views.news3, name='news3'),
    path('moreNews/', views.more_news, name='moreNews'),
]

