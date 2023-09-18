from django.db import models


class Card(models.Model):
    titulo = models.CharField(max_length=100)
    introducao = models.TextField(default="")
    descricao_codigo = models.TextField(default="")
    codigo = models.TextField(default="")
    conclusao = models.TextField(default="")
    imagem_card = models.ImageField(upload_to="cards/", blank=True)
    imagem_circuito = models.ImageField(upload_to="cards/", blank=True)
    imagem_principal_conteudo = models.ImageField(upload_to="cards/", blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.titulo


class MateriaisExperimento(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=False, blank=True)
    material = models.CharField(max_length=100)


class Circuito(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=False, blank=True)
    passo_a_passo_circuito = models.CharField(max_length=100)
