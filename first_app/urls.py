from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.profileuser, name='profile'),
    path('change-pass/', views.pass_change, name='passchange'),
    path('change-pass-without-old/', views.pass_change_without_old, name='reset'),
]