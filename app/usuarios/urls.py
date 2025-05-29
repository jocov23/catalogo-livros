from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('', views.login_usuario, name='login')


]