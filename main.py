import random
from cards import card, displayHand
from time import sleep
from players import Player

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
    cards = []
    players[player] = Player(playerName, position, cards)

cardDeck = {
            
    "A": ["club", "diamond", "heart", "spade"],
    "2": ["club", "diamond", "heart", "spade"],
    "3": ["club", "diamond", "heart", "spade"],
    "4": ["club", "diamond", "heart", "spade"],
    "5": ["club", "diamond", "heart", "spade"],
    "6": ["club", "diamond", "heart", "spade"],
    "7": ["club", "diamond", "heart", "spade"],
    "8": ["club", "diamond", "heart", "spade"],
    "9": ["club", "diamond", "heart", "spade"],
    "10": ["club", "diamond", "heart", "spade"],
    "J": ["club", "diamond", "heart", "spade"],
    "Q": ["club", "diamond", "heart", "spade"],
    "K": ["club", "diamond", "heart", "spade"]
    
    }

def printCard(suit, num): # takes suit(str) and value of card(str)
    if suit == "club":
        char = "♣"
    elif suit == "diamond":
        char = "♦"
    elif suit == "heart":
        char = "♥"
    elif suit == "spade":
        char = "♠"
    else:
        char = " "

    card(num, char)
    print(f'\n{num} of {suit}s\n')

def removeCard(suit, num): # takes suit(str) and value of card(str)
    cardDeck[f'{num}'].remove(suit)

def deckRemainder(): # prints all items in cardDeck
    for number in cardDeck:
        print(f'{number}: {cardDeck[f'{number}']}') 
    print("") 

def deckAnimation():
    s = "....."
    i=0
    while i < 5:
        i+=1
        print(s[0:i])
        sleep(.25)
    while i > 0:
        i-=1
        print(s[0:i])
        sleep(.25)

def deckAnimation2():
    s = "..................."
    i=0
    while i < 20:
        i+=2
        print(s[0:i])
        sleep(.05)
    while i > 0:
        i-=2
        print(s[0:i])
        sleep(.05)

def resetDeck():
    for num in cardDeck:
        cardDeck[num] = ["club", "diamond", "heart", "spade"]
    deckAnimation()
    deckAnimation2()
    deckAnimation()
    print('Deck is ready!')

def addCard_to_Player(suit, num, player):
    players[f'{player}'].receive_card(suit, num)
    #players[f'{player}'].get_cards()

def draw(player):
    while True:
        num = random.choice(list(cardDeck.keys()))
        empty = len(cardDeck[f'{num}'])
        if empty != 0:
            suit = random.choice(cardDeck[f'{num}'])
            break
    printCard(suit, num) 
    addCard_to_Player(suit, num, player)
    removeCard(suit, num)
    e=0
    for num in list(cardDeck.keys()):
        if len(cardDeck[f'{num}']) == 0:
            e+=1
    if e == 13:
        print("Card Deck is empty.\nReshuffling the deck...")
        resetDeck()

def display():
    t = 1
    print("\n~ ~ ~ Welcome to Cards ~ ~ ~\n")
    while True:
        if t>p:
            t = 1
        print(f"{playerList[(t-1)]}'s turn.\n")
        # print(players[f'{playerList[(t-1)]}'].get_playerName())
        choice = input("Choice:\n1. Draw card\n2. View hand\n3. Quit\n\n>> ").lower()
        print()
        if choice == '1':
            draw(playerList[(t-1)])
            t+=1
        elif choice == '2':
            #players[f'{player}'].get_cards()
            displayHand(players[f'{playerList[(t-1)]}'].get_cards())
        elif choice == '69':
            deckRemainder()
        else:
            break

display()
