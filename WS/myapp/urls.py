

from django.urls import path, include, re_path
from . import views
from .views import *

urlpatterns = [
    #Продукты\Товары
    path('prod/', product_all),
    path('prod/<int:pk>/', product_detail),
    #Заказы
    path('order/', order_all),
    path('order/<int:pk>', order_detail),
    #Работники
    path('worker/<int:pk>', worker_detail),
    path('worker/', worker_all),
    #Смены
    path('change/<int:pk>', change_detail),
    path('change/', change_all),
    #Авторизация
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]