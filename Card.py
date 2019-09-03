from random import sample

class Card():
    ''' Draw a card from a 52-card deck. '''

    def __init__(self, num_cards=1):
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cardnums = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.deck = [c + ' of ' + s for c in self.cardnums for s in self.suits]
        self.num_cards = num_cards

    def draw(self):
        ''' Draw a card. '''
        picks = sample(self.deck, self.num_cards)
        for pick in picks:
            print(pick)
