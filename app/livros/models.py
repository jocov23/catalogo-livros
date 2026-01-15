from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
       

#define the model to be send to the database
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    editora = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    slug=models.SlugField( blank=True, null=True, unique=True, max_length=200)
    imagem=models.ImageField(upload_to='livros/',null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            copia = 2
            while Livro.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}--{copia}"
                copia += 1
            self.slug = slug
        super().save(*args, **kwargs)

   


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
    
class Opiniao(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="opinions")
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Opinião de {self.livro.titulo} por {self.autor.username}"


