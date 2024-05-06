import random


class Card:
    """Generic cards class"""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit=suit

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit) 
    

class Deck:
    """Generic deck of cards class"""
    def __init__(self):
        # Initialize deck as a list of 52 cards
        self.cards = []
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def get_card(self):
        return self.cards.pop()
    