from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Deck
from .forms import DeckForm, LoginForm

# Create your views here.

def index(request):
    decks = Deck.objects.all()
    form = DeckForm()
    return render(request, 'index.html', {'decks':decks, 'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print('The account has been disabled!')
            else:
                print("The Username and Password are incorrect!")
    else:
        form = LoginForm()
        return render(request, 'login.html',
            {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    decks = Deck.objects.filter(user=user)
    form = DeckForm()
    return render(request, 'profile.html', {
                            'username': username,
                            'decks': decks,
                            'form': form,
    })

def detail(request, decks_id):
    decks = Deck.objects.get(id=decks_id)
    return render(request, 'detail.html', {'decks':decks})

def post_deck(request):
    form = DeckForm(request.POST, request.FILES)
    if form.is_valid():
        deck = form.save(commit = False)
        deck.user=request.user
        deck.save()

    return HttpResponseRedirect('/')
