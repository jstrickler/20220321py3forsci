"""
Provide a class for playing cards
"""
import random

class CardDeck:  # inherits from 'object'
    """
    A deck of cards.

    Has the usual features:
       -- shuffle
       -- deal

    Can have a dealer name
    """
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'clubs diamonds hearts spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer  # private variable
        self._make_deck()

    def _make_deck(self):
        self._cards = []  # ._cards is a list
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit  # card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        """
        Randomize the deck

        :return: None
        """
        random.shuffle(self._cards)

    def draw(self):
        """
        Deal one card from the deck

        :return: one card, as a tuple
        """
        return self._cards.pop()

    @property
    def cards(self):
        """
        The list of cards (as tuples)
        """
        return self._cards

    @property
    def dealer(self):   # public variable (read-only by default)
        """
        The current dealer
        """
        return self._dealer   # 'getter' property

    @dealer.setter
    def dealer(self, dealer):   # 'setter' property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def __str__(self):
        return f"Deck: {self.dealer}/{len(self._cards)}"
