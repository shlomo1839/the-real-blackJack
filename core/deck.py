
from random import randint


def build_standard_deck() -> list[dict]:
    deck = []
    for suit in ["H", "C", "D", "S"]:
        for i in range(2, 11):
            deck.append({'rank' : str(i), 'suit' : suit})
        for high_rank in ['J', 'Q', 'K', 'A']:
            deck.append({'rank' : high_rank, 'suit' : suit})
    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range (swaps):
        condition = False
        while not condition:
            i = randint(0, len(deck)-1)
            suit = deck[i]['suit']
            j = randint(0, len(deck) -1)
            not_equal = i != j
            if suit == 'H':
                condition = not j % 5
            elif suit == 'C':
                condition = not j % 3
            elif suit == 'D':
                condition = not j % 2
            elif suit == 'S':
                condition = not j % 7
            else:
                condition = ''
            is_math = not_equal and condition
        deck[i], deck[j] = deck[j], deck[i]
    return deck