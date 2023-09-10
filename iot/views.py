from django.shortcuts import render
from .models import Card


def index(request):
    cards = Card.objects.all()
    return render(request, 'iot/index.html', {'cards': cards})
