
from django.urls import path
from . import views

#This file allows you to create urls for each page on the website.
#Each seperate page in the website should be have a seperate URL.


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]

