from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Livro
from .serializers import LivroSerializer

#function to create or request data from a book
@api_view(['GET', 'POST'])
def livros_list(request):
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Function to modify or request data of a already existing book
@api_view(['GET', 'PUT', 'DELETE'])
def livro_detail(request, pk):
    # Verify if the book requested is contained in the database (pk= primarykey)j
    try:
        livro = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
            return Response({'erro': 'Livro nao encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #if method is DELETE, it just...delete    
    elif request.method == 'DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
    