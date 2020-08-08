from card import Card
import random

Suitlist = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
Ranklist = ('Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
Valuelist = {'Ace':1,'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}
class Deck:

    def __init__(self,suit,rank,value):
        self.all_card = {}
        
        for symbol in suit:
            for num in rank:
                mycard = Card(symbol,num,value[num])
                self.all_card.update(mycard.get_value())

    def shaffle(self):
        random.shuffle(self.all_card)

    def deal_one(self):
        self.all_card.pop()


