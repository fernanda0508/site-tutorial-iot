from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Card, Favorite


def index(request):
    cards = Card.objects.all()
    return render(request, "iot/index.html", {"cards": cards})


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
            # Autenticar o usuário após o cadastro
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(
                    "index"
                )  # Redirecionar para a página inicial após o cadastro
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
    card = Card.objects.get(pk=card_id)

    # Verifique se o card já está nos favoritos do usuário
    if request.user.is_authenticated:
        if card.is_favorited_by(request.user):
            # O card já estava nos favoritos, então agora o usuário deseja removê-lo
            Favorite.objects.filter(user=request.user, card=card).delete()
        else:
            # O card não estava nos favoritos, então o usuário deseja adicioná-lo
            Favorite.objects.create(user=request.user, card=card)

    # Adicione instruções de depuração para verificar se a view está sendo chamada
    # corretamente e se as operações estão ocorrendo como esperado.
    print(f"Card ID: {card_id}")
    print(f"User: {request.user}")

    # Adicione mais instruções de depuração conforme necessário.

    return redirect("index")


@login_required
def favorites(request):
    # recupera os favoritos do usuário e renderiza a página de favoritos.
    user_favorites = Favorite.objects.filter(user=request.user)
    return render(request, "iot/favorites.html", {"user_favorites": user_favorites})
