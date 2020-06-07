from random import shuffle
from cards import Cards

class Deck():
    def __init__(self):
        self.cards = list()
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Cards(i,j))
        shuffle(self.cards)        
    def rm_cards(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player():
    def __init__(self, name):
        self.win = 0
        self. card = None
        self.name = name