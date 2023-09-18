from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Card


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
