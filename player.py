from deck import Deck

Suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
Ranks = ('Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
Values = {'Ace':1,'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

class Player:

    def __init__(self,cards):
        self.cards = cards
        self.status = 'active'
        

    def hit(self,cards):
        self.cards.update(cards)

    def calculate_point(self):
        for suit,rank in self.cards:
            if rank == 'Ace':
                score += self.get_Ace_value()
            else:
                score += Values[rank] 
           
    def get_Ace_value(self):
         if len(self.cards <= 2):
                return 11
            else:
                return 1 

    def set_status(self,status):
        self.status = status
    
    def get_status(self):
        return self.status


        