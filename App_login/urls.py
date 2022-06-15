from django.urls import path
from . import views

app_name = 'App_login'


urlpatterns = [
    path('new_user/', views.signup, name='signup'),
    path('login/', views.login_sys, name='login'),
    path('logout/', views.logout_sys, name='logout',)


]
