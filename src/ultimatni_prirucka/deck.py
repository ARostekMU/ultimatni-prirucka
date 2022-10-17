from collections import namedtuple
from dataclasses import dataclass
from collections.abc import MutableSequence


@dataclass(frozen=True)
class Card:
    colour: str
    value: str


@dataclass(frozen=True)
class ToggleCard(Card):
    is_revealed: bool = False


#Card = namedtuple("Card", ["colour", "value"])


class Deck(MutableSequence):
    values = [str(n) for n in range(2, 11)] + list('JQKA')
    colours = ['diamond', 'spade', 'club', 'heart']

    def __delitem__(self, i):
        del self._cards[i]
    
    def __setitem__(self, i, o):
        self._cards[i] = o

    def insert(self, i, o):
        self._cards.insert(i, o)

    def __init__(self, card_factory=Card):
        self._cards = [
            card_factory(colour, value)
            for colour in Deck.colours
            for value in Deck.values
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]