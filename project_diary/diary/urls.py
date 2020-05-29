from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('', views.introduction, name="introduction"),
    path('login/', views.login, name='login'),
    path('editor/', views.editor, name='editor')
]
