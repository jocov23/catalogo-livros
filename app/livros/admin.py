from django.contrib import admin
from .models import Livro
# Register your models here.

admin.site.register(Livro)

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao', 'editora')
    search_fields = ( 'titulo', 'autor')