from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DECK_COST_RANGE =(
    ('B', 'Budget Standard Deck'),
    ('M', 'Average Cost Standard Deck'),
    ('E', 'Expensive Standart Deck'),
    ('U', 'Unknown / Yet to be Determined')
)

class DecksQuerySet(models.QuerySet):
    def deck_for_user(self, user):

        return self.filter(
            Q(deckname=user)
        )
class Deck(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    deckname = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank = True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False)
    price = models.CharField(max_length=1, default='U', choices=DECK_COST_RANGE)
    image = models.ImageField(upload_to="deck_images",
                              default='media/default.png')

    objects = DecksQuerySet.as_manager()

    def __str__(self):
        return '{0}'.format(self.deckname)

class Card(models.Model):
    cardname = models.CharField(max_length=50, blank=True)
    manacost = models.CharField(max_length=50, blank=True)
    set_name = models.CharField(max_length=50, blank=True)
    card_price = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '{0}'.format(self.cardname)


