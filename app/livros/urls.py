from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import livros_list, livro_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #HTML Interface 
    path('lista/', views.lista_livros, name='lista_livros'), #url to show books data
    path('cadastro_livros/', views.cadastro_livro, name='cadastro_livro'), #url to register book data
    path('detalhes_livro/<slug:slug>/', views.detalhes_livro, name='detalhes_livro'), #url to show book's details
    path('opiniao_livro/<slug:slug>/', views.opiniao_livro, name='opiniao_livro'), #url to show book's opinion
    path('contato/', views.contato, name='contato'), #url to show my info
    path('add_capa/<slug:slug>/', views.add_capa, name='add_capa'), #url to add book's cover
    

    #API Interface
    path('api/livros/', livros_list), #especific route to list or create in JSON
    path('api/livros/<int:pk>/', livro_detail),  #especific route to show, modify or delete data in JSON
]

