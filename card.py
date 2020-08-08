class Card:
    
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return self.rank + ' Of ' + self.suit

    def get_value(self):
        return {self.suit : self.rank}


