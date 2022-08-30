from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/<str:first_num><str:operator><str:second_num>', views.result, name='result'),
    path('calculate/', views.calculate, name='calculate'),
    path('result/clear/', views.clear, name='clear'),
    path('result/calculate/', views.calculate, name='calculate')
]
