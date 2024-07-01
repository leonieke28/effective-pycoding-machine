import string
from collections import namedtuple
import random

ACTIONS = ["draw_card", "play_again", "interchange_cards", "change_turn_direction"]
NUMBERS = range(1, 5)
LETTERS = list(string.ascii_uppercase)

PawCard = namedtuple("PawCard", "card action")


def create_paw_deck(n=8):
    if n > 26:
        raise ValueError

    # Stap 1: Kaarten genereren
    cards = [f"{letter}{num}" for letter in LETTERS[:n] for num in NUMBERS]

    # Stap 2: Acties toewijzen
    total_cards = n * 4
    actions = [None] * total_cards
    for i in range(3, total_cards, 4):
        actions[i] = random.choice(ACTIONS)
    random.shuffle(actions)

    # Stap 3: Kaarten en acties combineren
    deck = [PawCard(card, action) for card, action in zip(cards, actions)]

    return deck
