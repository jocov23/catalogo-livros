from django.db import models
from django.contrib.auth.models import User

#define the model to be send to the database
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    editora = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    #register its mention by its own title
    def __str__(self):
        return self.titulo
    
class Sinopse(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="sinopses")
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Sinopse de {self.livro.titulo} por {self.autor.username}"


