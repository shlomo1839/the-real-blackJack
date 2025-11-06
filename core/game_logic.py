from core.player_io import ask_player_action
import random

def calculate_hand_value(hand: list[dict]) -> int:
    total = 0
    for card in hand:
        if card['rank'] in ['J', 'Q', 'K']:
            total += 10
        elif card['rank'] == 'A':
            total += 1
        else:
            # without this casting There will be an error because it is a str
            total += int(card['rank'])
    return total
    

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    card_player1 = deck.pop()
    card_player2 = deck.pop()
    player["hand"].append(card_player1)
    player["hand"].append(card_player2)
    print(f'hand player: {calculate_hand_value(player['hand'])}')
    card_deler1 = deck.pop()
    card_dealer2 = deck.pop()
    dealer["hand"].append(card_deler1)
    dealer["hand"].append(card_dealer2)
    print(f'hand dealer: {calculate_hand_value(dealer['hand'])}')


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer['hand']) <= 17:
        dealer['hand'].append(deck.pop())
    if calculate_hand_value(dealer['hand']) > 21 :
        print('the dialer lose')
        return False
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    game_run = True
    player_action = None
    while game_run and player_action != 'S':
        ask_player_action = ask_player_action()
        if player_action == 'H':
            player['hand'].append(deck.pop())
            player_score = calculate_hand_value(player['hand'])
            if player_score > 21:
                game_run = False
                print()
                print('Game Over! dealer win')
                print("player's hand :", calculate_hand_value(player['hand']))
                # add dealer info
                return
    dealer_torn = dealer_play(deck, dealer)
    if dealer_torn:
        if calculate_hand_value(dealer['hand']) > calculate_hand_value(player['hand']):
            print('the dealer win')
        elif calculate_hand_value(dealer['hand']) < calculate_hand_value(player['hand']):
            print('player win')
        else:
            print('pik a card')
    else:
        print('the player win')
    print("player's hand :", calculate_hand_value(player['hand']))
    print("dealer's hand :", calculate_hand_value(dealer['hand']))