from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('', views.login_usuario, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


]