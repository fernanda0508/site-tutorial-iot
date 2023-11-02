from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Card, Favorite, MensagemDeContato


def index(request):
    cards = Card.objects.all()
    favorite_card_ids = []
    if request.user.is_authenticated:
        favorite_card_ids = request.user.favorite_set.values_list("card_id", flat=True)
    return render(
        request,
        "iot/index.html",
        {"cards": cards, "favorite_card_ids": favorite_card_ids},
    )


def tutorial_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, "iot/conteudo_card.html", {"card": card})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(
                "index"
            )  # Redirecione para a página do painel após o login bem-sucedido
        else:
            # Exiba uma mensagem de erro caso a autenticação falhe
            error_message = "Credenciais inválidas. Tente novamente."
            return render(request, "iot/login.html", {"error_message": error_message})
    else:
        return render(request, "iot/login.html")


def cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(
                "index"
            )  # Redirecione para a página inicial ou outra página desejada após o registro
    else:
        form = UserCreationForm()
    return render(request, "iot/cadastro.html", {"form": form})


def buscar(request):
    cards = Card.objects.all()
    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            cards = cards.filter(titulo__icontains=nome_a_buscar)
    return render(request, "iot/buscar.html", {"cards": cards})


def add_to_favorites(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    if request.user.is_authenticated:
        favorite, created = Favorite.objects.get_or_create(user=request.user, card=card)
        if not created:
            # O card já estava nos favoritos, então agora o usuário deseja removê-lo
            favorite.delete()
    return redirect(request.META.get("HTTP_REFERER"))


@login_required
def favorites(request):
    # Recupera os favoritos do usuário e renderiza a página de favoritos.
    user_favorites = Favorite.objects.select_related("card").filter(user=request.user)
    return render(request, "iot/favorites.html", {"user_favorites": user_favorites})


def contato(request):
    if request.method == "POST":
        nome = request.POST["name"]
        email = request.POST["email"]
        mensagem = request.POST["message"]
        data_envio = datetime.now()

        mensagem_contato = MensagemDeContato(
            nome=nome, email=email, mensagem=mensagem, data_envio=data_envio
        )
        mensagem_contato.save()
        return render(request, "iot/contato_sucesso.html")

        # Pode adicionar a lógica para enviar um e-mail aqui, se necessário.

    return render(request, "iot/contato.html")
