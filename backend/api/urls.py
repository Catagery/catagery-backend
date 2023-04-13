
from django.urls import path
from .import views

urlpatterns = [
    path('statistic/', views.main_page, name='index'),
    path('category_grafic/', views.get_rangom_grafic_info, name='random_category_grafic'),
    path('top_categories/', views.get_top_categories, name='top_categories'),
    path('category_grafic/<str:category>/', views.get_grafic_info, name='category_grafic'),
]