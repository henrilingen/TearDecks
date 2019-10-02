from django import forms
from .models import Deck

DECK_COST_RANGE =(
    ('B', 'Budget Standard Deck'),
    ('M', 'Average Cost Standard Deck'),
    ('E', 'Expensive Standart Deck'),
    ('U', 'Unknown / Yet to be Determined')
)

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['deckname', 'color', 'date_created', 'price', 'image']
        widgets = {
            'date_created': forms.SelectDateWidget(),
        }
    
    
    
    # deckname = forms.CharField(label='Deckname', max_length=50, required=True)
    # color = forms.CharField(label='Deck colors', max_length=50, required=True)
    # date_created = forms.DateTimeField(label='Date created', widget=forms.SelectDateWidget, required=False)
    # price = forms.CharField(label='Deck price', max_length=50, required=False)
    # img_url = forms.CharField(label='Image URL', max_length=500, required=False)