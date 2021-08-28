from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('process_money', views.process_money),
    ]
