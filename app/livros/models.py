from django.db import models

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

