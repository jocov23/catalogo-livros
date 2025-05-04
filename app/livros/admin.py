from django.contrib import admin
from .models import Livro

#register the "Livro" model in the admin configuration inside the site 
admin.site.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao', 'editora')
    search_fields = ( 'titulo', 'autor')