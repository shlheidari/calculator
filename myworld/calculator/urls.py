from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<data>', views.result, name='result'),
    path('calculate/', views.calculate, name='calculate'),
    path('result/clear/', views.clear, name='clear'),
    path('result/calculate/', views.calculate, name='calculate')
]
