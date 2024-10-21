from deckmanager import draw, deckRemainder
from players import Player

def intialize():
    while True:
        try:
            p = int(input('\nEnter number of players:\n>> '))
        except ValueError:
            print(f"Value must be integer.")
        else:
            break
    i = 0
    playerList = []
    while i < p:
        i+=1
        playerList.append(f'Player {i}')

    players = {}
    for player in playerList:
        playerName = player
        position = (playerList.index(player)) + 1
        cards = {}
        players[player] = Player(playerName, position, cards)


def display():
    t = 1
    print("\n~ ~ ~ Welcome to Cards ~ ~ ~\n")
    while True:
        if t>p:
            t = 1
        print(f"{playerList[(t-1)]}'s turn.\n")
        # print(players[f'{playerList[(t-1)]}'].get_playerName())
        choice = input("Choice:\n1. Draw card\n2. View remaining deck\n3. Quit\n\n>> ").lower()
        print()
        if choice == '1':
            draw(playerList[(t-1)])
            
            t+=1
        elif choice == '2':
            deckRemainder()
        else:
            break

display()