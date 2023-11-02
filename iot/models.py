from django.db import models
from django.contrib.auth.models import User


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

    def is_favorited_by(self, user):
        return self.favorite_set.filter(user=user).exists()


class MateriaisExperimento(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=False, blank=True)
    material = models.CharField(max_length=100)


class Circuito(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=False, blank=True)
    passo_a_passo_circuito = models.CharField(max_length=100)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            "user",
            "card",
        )  # Isso garante que a combinação de usuário e card seja única

    def __str__(self):
        return f"{self.user.username} - {self.card.titulo}"


class MensagemDeContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
