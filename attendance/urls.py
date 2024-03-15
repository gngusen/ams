from django.urls import path
from . import views

urlpatterns = [
    path('attendance/view/', views.view_attendance, name='view_attendance'),
    path('attendance/new/', views.new_attendance, name='new_attendance'),
    path('', views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home')
]
