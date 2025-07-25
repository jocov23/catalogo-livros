# Generated by Django 5.2.4 on 2025-07-22 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_livro_sinopse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='sinopse',
        ),
        migrations.CreateModel(
            name='Sinopse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sinopses', to='livros.livro')),
            ],
        ),
    ]
