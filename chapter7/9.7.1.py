import random

class Dealer():
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.cards = []

    def deal_player(self, player):
        if player.mode == "hit":
            player.add(self.deck.get_card())

    def deal_self(self):
        self.add(self.deck.get_card())
    
    def add(self, card):
        self.cards.append(card)

class Player():
    def __init__(self):
        self.cards = []
        self.mode = "hit"

    def add(self, card):
        self.cards.append(card)

    def stand(self):
        self.mode = "stand"

    def calc_value(self):
        self.sum = 0
        for card in self.cards:
            if card.val == "A":
                self.sum += 11
            elif card.val in ("J", "Q", "K"):
                self.sum += 10
            else:
                self.sum += int(card.val)
        return self.sum

class Card():
    def __init__(self, val, pat):
        self.val = val
        self.pat = pat

class Deck():
    def __init__(self):
        self.createDeck()

    def get_card(self):
        return self.deck.pop()

    def createDeck(self):
        self.deck = []
        for val in "A", "2", "3", "4", "5", "6", "7", "8", "10", "J", "Q", "K":
            for pat in "clubs", "diamonds","hearts", "spades":
                self.deck.append(Card(val, pat))

        random.shuffle(self.deck)

def play_blackjack(num_players):
    deck = Deck()
    players = [Player() for _ in range(num_players)]
    dealer = Dealer(players, deck)

    for _ in range(3):
        for index, player in enumerate(players):
            if player.calc_value() < 21:
                dealer.deal_player(player)
            else:
                player.stand()
            print(player.calc_value(), index)

play_blackjack(3)