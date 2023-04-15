from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('results/', views.results, name='results'),
    path('location/<str:pk>/', views.location_detail, name='location_detail'),
]
