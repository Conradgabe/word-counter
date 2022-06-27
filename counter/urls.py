from django.urls import path
from .import views

# app_name = 'counter'

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
]