from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import livros_list, livro_detail

#here the urls patterns show in this manner in the website >> METHOD /api/livros/..
urlpatterns = [
    path('livros/', livros_list), #especific route to list or create
    path('livros/<int:pk>/', livro_detail),  #especific route to show, modify or delete data
]