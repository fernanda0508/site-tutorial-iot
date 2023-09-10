from django.db import models

class Card(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem_card = models.ImageField(upload_to='cards/')
    imagem_conteudo = models.ImageField(upload_to='cards/', blank=True)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo