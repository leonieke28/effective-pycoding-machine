from collections import namedtuple

SUITS = "Red Green Yellow Blue".split()

UnoCard = namedtuple("UnoCard", "suit name")


def create_uno_deck():
    """Create a deck of 108 Uno cards.
    Return a list of UnoCard namedtuples
    (for cards w/o suit use None in the namedtuple)"""
    deck = []
    for suit in SUITS:
        deck.append(UnoCard(suit, "0"))

        for name in range(1, 10):
            deck.extend([UnoCard(suit, str(name))] * 2)

        for name in "Skip Reverse DrawTwo".split():
            deck.extend([UnoCard(suit, name)] * 2)

    deck.extend([UnoCard(None, "Wild")] * 4)
    deck.extend([UnoCard(None, "Wild Draw Four")] * 4)

    return deck
