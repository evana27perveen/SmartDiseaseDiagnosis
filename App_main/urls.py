from django.urls import path
from . import views

app_name = 'App_main'


urlpatterns = [
    path('', views.home, name='home'),
    path('heart-disease/', views.heart_disease_detect, name='heart-disease'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
]
