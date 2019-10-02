from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Deck
from .forms import DeckForm

# Create your views here.

def index(request):
    decks = Deck.objects.all()
    form = DeckForm()
    return render(request, 'index.html', {'decks':decks, 'form':form})

def detail(request, decks_id):
    decks = Deck.objects.get(id=decks_id)
    return render(request, 'detail.html', {'decks':decks})

def post_deck(request):
    form = DeckForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = True)

    return HttpResponseRedirect('/')
