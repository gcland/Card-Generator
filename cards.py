import random

def printCard(suit, num):
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

    if num == "10":
        print(f"╔═══════════╗")
        print(f"║{num}         ║")
        print(f"║   {char}   {char}   ║")
        print(f"║     {char}     ║")
        print(f"║   {char}   {char}   ║")
        print(f"║   {char}   {char}   ║")
        print(f"║     {char}     ║")
        print(f"║   {char}   {char}   ║")
        print(f"║         {num}║")
        print(f"╚═══════════╝")
    
    else:
        print(f"╔═══════════╗")
        print(f"║ {num}         ║")
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")

suitList = ["club", "diamond", "heart", "spade"]
numList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

suitIndex = random.randint(0,3)
numIndex = random.randint(0,12)

print(f'\n{numList[numIndex]} of {suitList[suitIndex]}s\n')

printCard(suitList[suitIndex], numList[numIndex])