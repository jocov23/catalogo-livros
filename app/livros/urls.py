from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import livros_list, livro_detail

urlpatterns = [
    
    #HTML Interface 
    path('', views.listar_livros, name='listar_livros'), #url to show books data
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'), #url to register book data

    #API Interface
    path('api/livros/', livros_list), #especific route to list or create in JSON
    path('api/livros/<int:pk>/', livro_detail),  #especific route to show, modify or delete data in JSON
]