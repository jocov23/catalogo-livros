from django import forms
from .models import Livro

#transform Livro model in Form format (convert in HTML automatically by Django)
class LivroForm(forms.ModelForm):
    #class Meta indicates the main config of the class
    class Meta:
        model = Livro
        fields = ['titulo', 'autor','ano_publicacao', 'editora']
