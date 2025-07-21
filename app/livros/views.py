from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import LivroForm
from .models import Livro
from .serializers import LivroSerializer
#from django.contrib.auth.models import User
#from django.contrib import messages



def cadastro_livro(request): #HTML #submit book

    mensagem = ''

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get ('autor')
        ano_publicacao = request.POST.get ('ano_publicacao')
        editora = request.POST.get ('editora')

        if Livro.objects.filter(titulo=titulo, autor=autor).exists(): #verify if the book already exists
            mensagem = 'Este livro já foi adicionado!'
        else:
            Livro.objects.create(
                titulo=titulo,
                autor=autor,
                ano_publicacao=ano_publicacao,
                editora=editora
            )
            return redirect('lista_livros')
        
    return render(request, 'livros/cadastro_livro.html', {'mensagem': mensagem})

#function to list book data
def lista_livros(request): #HTML
    livros = Livro.objects.all().order_by('-criado_em')
    return render(request, 'livros/listar.html', {'livros':livros})

#function to show book detail
def detalhes_livro(request, livro_id):
    a

#---------------------------------------------------------------------------------------------------------------

#function to create or request data from a book
@api_view(['GET', 'POST']) #API
def livros_list(request):
    
    #show books by date of criation
    livros = Livro.objects.all().order_by('-criado_em')

    #If method created is "get" (to return some data), serializer convert the list of books in JSON and return to the user
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many = True)
        return Response(serializer.data)
    
    #If method is "POST" (to create some data), serializer verify if the format is valid and or create succesfully(send to the database) 
    # or return error 400
    elif request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

# Function to modify or request data of a already existing book
@api_view(['GET', 'PUT', 'DELETE']) #API
def livro_detail(request, pk):

    # Verify if the book requested is contained in the database (pk= primarykey)
    try:
        livro = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
            return Response({'erro': 'Livro nao encontrado'}, status=404)
    
    #request data from a especific book by method GET
    if request.method == 'GET':
        serializer=LivroSerializer(livro)
        return Response(serializer.data)
    
    #verify if data sent is valid and modify a especific book details, or send a error code
    if request.method == 'PUT':
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    #if method is DELETE, it just...delete    
    elif request.method == 'DELETE':
        livro.delete()
        return Response(status=204)       
    