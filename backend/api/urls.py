
from django.urls import path
from .import views

urlpatterns = [
    path('statistic/', views.index, name='index'),
]