from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, card_count, rounds, budget):
        self.card_count = card_count
        self.rounds = rounds
        self.name = name
        self.budget = budget

    def __repr__(self):
        return self.name

    @abstractmethod
    def decide(self, visible_cards, buy_price, sell_price):
        """return a tuple of (buy/sell, count), where 0 = sell and 1 = buy"""

        N = 52
        X = 416
        pred = 0
        self.card_count = 3

        buy_sell = True  ## buy 
        units = 0 

        number_cards_visable = len(visible_cards)

        N -= number_cards_visable
        
        for i in range(number_cards_visable):
            X -= visible_cards[i]
            Pred += visible_cards[i]

        E = X/N

        pred += E * (self.card_count - number_cards_visable)

        if buy_price <= pred:
             
            buy_sell = True
             
            units = (self.budget) / buy_price

            return(buy_sell,units)
        
        if sell_price >= pred:

            buy_sell = False

            units = (self.budget) / sell_price

            return(buy_sell,units)
        
        if sell_price < pred < buy_price:
            return (buy_sell, 0)


    @abstractmethod
    def reveal(self, cards):
        """shows the player what cards there are"""
        














    