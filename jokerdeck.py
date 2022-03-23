from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call _make_deck() in parent class
        for joker_number in '1', '2':
            card = joker_number, '**JOKER**'
            self._cards.append(card)


