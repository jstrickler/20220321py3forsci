import random

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = 'clubs diamonds hearts spades'.split()

def create_deck(dealer):
    cards = []
    for suit in SUITS:
        for rank in RANKS:
            card = rank, suit   # make a tuple
            cards.append(card)
    return cards

def shuffle_deck(deck):
    random.shuffle(deck)

def draw_card(deck):
    return deck.pop()


d = create_deck("Amanda")  # d['cards']  d['dealer']
shuffle_deck(d)
print(draw_card(d))
print()
print(d)

d2 = create_deck("Fred")
shuffle_deck(d)
