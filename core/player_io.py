def ask_player_action() -> str:
    request = None
    while not request in ['S', 'H']:
        request = input("please enter 'H' or 's'")
    return request
