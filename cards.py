def card(num, char):
    if num == "A":
        print(f"╔═══════════╗")
        print(f"║ {num}         ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")

    elif num == "3":
        print(f"╔═══════════╗")
        print(f"║ {num}         ║")
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")
    
    elif num == "4":
        print(f"╔═══════════╗")
        print(f"║ {num}         ║")
        print(f"║   {char}   {char}   ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║   {char}   {char}   ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")

    elif num == "5":
        print(f"╔═══════════╗")
        print(f"║ {num}         ║")
        print(f"║   {char}   {char}   ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║   {char}   {char}   ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")
    
    elif num == "6":
        print(f"╔═══════════╗")
        print(f"║ {num}         ║")
        print(f"║   {char}   {char}   ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║   {char}   {char}   ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║   {char}   {char}   ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")

    elif num == "7":
        print(f"╔═══════════╗")
        print(f"║ {num}         ║")
        print(f"║   {char}   {char}   ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║   {char}   {char}   ║")
        print(f"║           ║")
        print(f"║           ║")
        print(f"║   {char}   {char}   ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")
    
    elif num == "8":
        print(f"╔═══════════╗")
        print(f"║ {num}         ║")
        print(f"║   {char}   {char}   ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║   {char}   {char}   ║")
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║   {char}   {char}   ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")
    
    elif num == "9":
        print(f"╔═══════════╗")
        print(f"║ {num}         ║")
        print(f"║   {char}   {char}   ║")
        print(f"║   {char}   {char}   ║")
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║   {char}   {char}   ║")
        print(f"║   {char}   {char}   ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")

    elif num == "10":
        print(f"╔═══════════╗")
        print(f"║{num}         ║")
        print(f"║   {char}   {char}   ║")
        print(f"║     {char}     ║")
        print(f"║   {char}   {char}   ║")
        print(f"║           ║")
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
        print(f"║           ║")
        print(f"║     {char}     ║")
        print(f"║           ║")
        print(f"║         {num} ║")
        print(f"╚═══════════╝")

def displayHand(cards):

    if len(cards) > 4:
        print(cards)
    if len(cards) == 0:
        print("Your hand is empty.")

    #if hand has 1 card
    if len(cards) == 1:
        number1 = cards[0][0]
        char1 = cards[0][1]
        if number1 == 'A':
            numKey1 = 'numAce1'
        elif number1 == '3':
            numKey1 = 'num3_1'
        elif number1 == '4':
            numKey1 = 'num4_1'
        elif number1 == '5':
            numKey1 = 'num5_1'
        elif number1 == '6':
            numKey1 = 'num6_1'
        elif number1 == '7':
            numKey1 = 'num7_1'
        elif number1 == '8':
            numKey1 = 'num8_1'
        elif number1 == '9':
            numKey1 = 'num9_1'
        elif number1 == '1':
            number1 = '10'
            char1 = cards[0][2]
            numKey1 = 'num10_1'
        else:
            numKey1 = 'numFace1'

        numberDict = {
        
        "numAce1": (f"╔═══════════╗║ {number1}         ║║           ║║           ║║           ║║     {char1}     ║║           ║║           ║║           ║║         {number1} ║╚═══════════╝"),

        "numFace1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║           ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),

        "num3_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),

        "num4_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),

        "num5_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),

        "num6_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),

        "num7_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        
        "num8_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),

        "num9_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),

        "num10_1": (f"╔═══════════╗║ {number1}        ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║        {number1} ║╚═══════════╝"),
        
        }

        print(f'{numberDict[f"{numKey1}"][0:13]}')   
        print(f'{numberDict[f"{numKey1}"][13:26]}')  
        print(f'{numberDict[f"{numKey1}"][26:39]}')   
        print(f'{numberDict[f"{numKey1}"][39:52]}')    
        print(f'{numberDict[f"{numKey1}"][52:65]}')    
        print(f'{numberDict[f"{numKey1}"][65:78]}')    
        print(f'{numberDict[f"{numKey1}"][78:91]}')   
        print(f'{numberDict[f"{numKey1}"][91:104]}')    
        print(f'{numberDict[f"{numKey1}"][104:117]}')    
        print(f'{numberDict[f"{numKey1}"][117:130]}')    
        print(f'{numberDict[f"{numKey1}"][130:143]}')

    # if hand has 2 cards
    if len(cards) == 2:
        number1 = cards[0][0]
        char1 = cards[0][1]
        if number1 == 'A':
            numKey1 = 'numAce1'
        elif number1 == '3':
            numKey1 = 'num3_1'
        elif number1 == '4':
            numKey1 = 'num4_1'
        elif number1 == '5':
            numKey1 = 'num5_1'
        elif number1 == '6':
            numKey1 = 'num6_1'
        elif number1 == '7':
            numKey1 = 'num7_1'
        elif number1 == '8':
            numKey1 = 'num8_1'
        elif number1 == '9':
            numKey1 = 'num9_1'
        elif number1 == '1':
            number1 = '10'
            char1 = cards[0][2]
            numKey1 = 'num10_1'
        else:
            numKey1 = 'numFace1'

        number2 = cards[1][0]
        char2 = cards[1][1]
        if number2 == 'A':
            numKey2 = 'numAce2'
        elif number2 == '3':
            numKey2 = 'num3_2'
        elif number2 == '4':
            numKey2 = 'num4_2'
        elif number2 == '5':
            numKey2 = 'num5_2'
        elif number2 == '6':
            numKey2 = 'num6_2'
        elif number2 == '7':
            numKey2 = 'num7_2'
        elif number2 == '8':
            numKey2 = 'num8_2'
        elif number2 == '9':
            numKey2 = 'num9_2'
        elif number2 == '1':
            number2 = '10'
            char2 = cards[1][2]
            numKey2 = 'num10_2'
        else:
            numKey2 = 'numFace2'

        numberDict = {
        
        "numAce1": (f"╔═══════════╗║ {number1}         ║║           ║║           ║║           ║║     {char1}     ║║           ║║           ║║           ║║         {number1} ║╚═══════════╝"),
        "numAce2": (f"╔═══════════╗║ {number2}         ║║           ║║           ║║           ║║     {char2}     ║║           ║║           ║║           ║║         {number2} ║╚═══════════╝"),

        "numFace1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║           ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "numFace2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║           ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),

        "num3_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num3_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),

        "num4_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num4_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),

        "num5_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num5_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),

        "num6_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num6_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),

        "num7_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num7_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        
        "num8_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num8_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),

        "num9_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num9_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),

        "num10_1": (f"╔═══════════╗║ {number1}        ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║        {number1} ║╚═══════════╝"),
        "num10_2": (f"╔═══════════╗║ {number2}        ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║        {number2} ║╚═══════════╝"),
        
        }

        print(f'{numberDict[f"{numKey1}"][0:13]}     {numberDict[f"{numKey2}"][0:13]}')
        print(f'{numberDict[f"{numKey1}"][13:26]}     {numberDict[f"{numKey2}"][13:26]}')
        print(f'{numberDict[f"{numKey1}"][26:39]}     {numberDict[f"{numKey2}"][26:39]}')
        print(f'{numberDict[f"{numKey1}"][39:52]}     {numberDict[f"{numKey2}"][39:52]}')
        print(f'{numberDict[f"{numKey1}"][52:65]}     {numberDict[f"{numKey2}"][52:65]}')
        print(f'{numberDict[f"{numKey1}"][65:78]}     {numberDict[f"{numKey2}"][65:78]}')
        print(f'{numberDict[f"{numKey1}"][78:91]}     {numberDict[f"{numKey2}"][78:91]}')
        print(f'{numberDict[f"{numKey1}"][91:104]}     {numberDict[f"{numKey2}"][91:104]}')
        print(f'{numberDict[f"{numKey1}"][104:117]}     {numberDict[f"{numKey2}"][104:117]}')
        print(f'{numberDict[f"{numKey1}"][117:130]}     {numberDict[f"{numKey2}"][117:130]}')
        print(f'{numberDict[f"{numKey1}"][130:143]}     {numberDict[f"{numKey2}"][130:143]}')

    # if hand has 3 cards
    if len(cards) == 3:
        number1 = cards[0][0]
        char1 = cards[0][1]
        if number1 == 'A':
            numKey1 = 'numAce1'
        elif number1 == '3':
            numKey1 = 'num3_1'
        elif number1 == '4':
            numKey1 = 'num4_1'
        elif number1 == '5':
            numKey1 = 'num5_1'
        elif number1 == '6':
            numKey1 = 'num6_1'
        elif number1 == '7':
            numKey1 = 'num7_1'
        elif number1 == '8':
            numKey1 = 'num8_1'
        elif number1 == '9':
            numKey1 = 'num9_1'
        elif number1 == '1':
            number1 = '10'
            char1 = cards[0][2]
            numKey1 = 'num10_1'
        else:
            numKey1 = 'numFace1'
            
        number2 = cards[1][0]
        char2 = cards[1][1]
        if number2 == 'A':
            numKey2 = 'numAce2'
        elif number2 == '3':
            numKey2 = 'num3_2'
        elif number2 == '4':
            numKey2 = 'num4_2'
        elif number2 == '5':
            numKey2 = 'num5_2'
        elif number2 == '6':
            numKey2 = 'num6_2'
        elif number2 == '7':
            numKey2 = 'num7_2'
        elif number2 == '8':
            numKey2 = 'num8_2'
        elif number2 == '9':
            numKey2 = 'num9_2'
        elif number2 == '1':
            number2 = '10'
            char2 = cards[1][2]
            numKey2 = 'num10_2'
        else:
            numKey2 = 'numFace2'

        number3 = cards[2][0]
        char3 = cards[2][1]
        if number3 == 'A':
            numKey3 = 'numAce3'
        elif number3 == '3':
            numKey3 = 'num3_3'
        elif number3 == '4':
            numKey3 = 'num4_3'
        elif number3 == '5':
            numKey3 = 'num5_3'
        elif number3 == '6':
            numKey3 = 'num6_3'
        elif number3 == '7':
            numKey3 = 'num7_3'
        elif number3 == '8':
            numKey3 = 'num8_3'
        elif number3 == '9':
            numKey3 = 'num9_3'
        elif number3 == '1':
            number3 = '10'
            char3 = cards[2][2]
            numKey3 = 'num10_3'
        else:
            numKey3 = 'numFace3'

        numberDict = {
        
        "numAce1": (f"╔═══════════╗║ {number1}         ║║           ║║           ║║           ║║     {char1}     ║║           ║║           ║║           ║║         {number1} ║╚═══════════╝"),
        "numAce2": (f"╔═══════════╗║ {number2}         ║║           ║║           ║║           ║║     {char2}     ║║           ║║           ║║           ║║         {number2} ║╚═══════════╝"),
        "numAce3": (f"╔═══════════╗║ {number3}         ║║           ║║           ║║           ║║     {char3}     ║║           ║║           ║║           ║║         {number3} ║╚═══════════╝"),

        "numFace1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║           ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "numFace2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║           ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "numFace3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║           ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),

        "num3_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num3_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num3_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),

        "num4_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num4_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num4_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),

        "num5_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num5_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num5_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),

        "num6_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num6_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num6_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),

        "num7_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num7_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num7_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),
        
        "num8_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num8_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num8_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),

        "num9_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num9_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num9_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),

        "num10_1": (f"╔═══════════╗║ {number1}        ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║        {number1} ║╚═══════════╝"),
        "num10_2": (f"╔═══════════╗║ {number2}        ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║        {number2} ║╚═══════════╝"),
        "num10_3": (f"╔═══════════╗║ {number3}        ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║        {number3} ║╚═══════════╝"),
        
        }

        print(f'{numberDict[f"{numKey1}"][0:13]}     {numberDict[f"{numKey2}"][0:13]}     {numberDict[f"{numKey3}"][0:13]}')
        print(f'{numberDict[f"{numKey1}"][13:26]}     {numberDict[f"{numKey2}"][13:26]}     {numberDict[f"{numKey3}"][13:26]}')
        print(f'{numberDict[f"{numKey1}"][26:39]}     {numberDict[f"{numKey2}"][26:39]}     {numberDict[f"{numKey3}"][26:39]}')
        print(f'{numberDict[f"{numKey1}"][39:52]}     {numberDict[f"{numKey2}"][39:52]}     {numberDict[f"{numKey3}"][39:52]}')
        print(f'{numberDict[f"{numKey1}"][52:65]}     {numberDict[f"{numKey2}"][52:65]}     {numberDict[f"{numKey3}"][52:65]}')
        print(f'{numberDict[f"{numKey1}"][65:78]}     {numberDict[f"{numKey2}"][65:78]}     {numberDict[f"{numKey3}"][65:78]}')
        print(f'{numberDict[f"{numKey1}"][78:91]}     {numberDict[f"{numKey2}"][78:91]}     {numberDict[f"{numKey3}"][78:91]}')
        print(f'{numberDict[f"{numKey1}"][91:104]}     {numberDict[f"{numKey2}"][91:104]}     {numberDict[f"{numKey3}"][91:104]}')
        print(f'{numberDict[f"{numKey1}"][104:117]}     {numberDict[f"{numKey2}"][104:117]}     {numberDict[f"{numKey3}"][104:117]}')
        print(f'{numberDict[f"{numKey1}"][117:130]}     {numberDict[f"{numKey2}"][117:130]}     {numberDict[f"{numKey3}"][117:130]}')
        print(f'{numberDict[f"{numKey1}"][130:143]}     {numberDict[f"{numKey2}"][130:143]}     {numberDict[f"{numKey3}"][130:143]}')



    # if hand has 4 cards
    if len(cards) == 4:

        number1 = cards[0][0]
        char1 = cards[0][1]
        if number1 == 'A':
            numKey1 = 'numAce1'
        elif number1 == '3':
            numKey1 = 'num3_1'
        elif number1 == '4':
            numKey1 = 'num4_1'
        elif number1 == '5':
            numKey1 = 'num5_1'
        elif number1 == '6':
            numKey1 = 'num6_1'
        elif number1 == '7':
            numKey1 = 'num7_1'
        elif number1 == '8':
            numKey1 = 'num8_1'
        elif number1 == '9':
            numKey1 = 'num9_1'
        elif number1 == '1':
            number1 = '10'
            char1 = cards[0][2]
            numKey1 = 'num10_1'
        else:
            numKey1 = 'numFace1'
            
        number2 = cards[1][0]
        char2 = cards[1][1]
        if number2 == 'A':
            numKey2 = 'numAce2'
        elif number2 == '3':
            numKey2 = 'num3_2'
        elif number2 == '4':
            numKey2 = 'num4_2'
        elif number2 == '5':
            numKey2 = 'num5_2'
        elif number2 == '6':
            numKey2 = 'num6_2'
        elif number2 == '7':
            numKey2 = 'num7_2'
        elif number2 == '8':
            numKey2 = 'num8_2'
        elif number2 == '9':
            numKey2 = 'num9_2'
        elif number2 == '1':
            number2 = '10'
            char2 = cards[1][2]
            numKey2 = 'num10_2'
        else:
            numKey2 = 'numFace2'

        number3 = cards[2][0]
        char3 = cards[2][1]
        if number3 == 'A':
            numKey3 = 'numAce3'
        elif number3 == '3':
            numKey3 = 'num3_3'
        elif number3 == '4':
            numKey3 = 'num4_3'
        elif number3 == '5':
            numKey3 = 'num5_3'
        elif number3 == '6':
            numKey3 = 'num6_3'
        elif number3 == '7':
            numKey3 = 'num7_3'
        elif number3 == '8':
            numKey3 = 'num8_3'
        elif number3 == '9':
            numKey3 = 'num9_3'
        elif number3 == '1':
            number3 = '10'
            char3 = cards[2][2]
            numKey3 = 'num10_3'
        else:
            numKey3 = 'numFace3'

        number4 = cards[3][0]
        char4 = cards[3][1]
        if number4 == 'A':
            numKey4 = 'numAce4'
        elif number4 == '3':
            numKey4 = 'num3_4'
        elif number4 == '4':
            numKey4 = 'num4_4'
        elif number4 == '5':
            numKey4 = 'num5_4'
        elif number4 == '6':
            numKey4 = 'num6_4'
        elif number4 == '7':
            numKey4 = 'num7_4'
        elif number4 == '8':
            numKey4 = 'num8_4'
        elif number4 == '9':
            numKey4 = 'num9_4'
        elif number4 == '1':
            number4 = '10'
            char4 = cards[3][2]
            numKey4 = 'num10_4'
        else:
            numKey4 = 'numFace4'

        numberDict = {
        
        "numAce1": (f"╔═══════════╗║ {number1}         ║║           ║║           ║║           ║║     {char1}     ║║           ║║           ║║           ║║         {number1} ║╚═══════════╝"),
        "numAce2": (f"╔═══════════╗║ {number2}         ║║           ║║           ║║           ║║     {char2}     ║║           ║║           ║║           ║║         {number2} ║╚═══════════╝"),
        "numAce3": (f"╔═══════════╗║ {number3}         ║║           ║║           ║║           ║║     {char3}     ║║           ║║           ║║           ║║         {number3} ║╚═══════════╝"),
        "numAce4": (f"╔═══════════╗║ {number4}         ║║           ║║           ║║           ║║     {char4}     ║║           ║║           ║║           ║║         {number4} ║╚═══════════╝"),

        "numFace1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║           ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "numFace2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║           ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "numFace3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║           ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),
        "numFace4": (f"╔═══════════╗║ {number4}         ║║           ║║     {char4}     ║║           ║║           ║║           ║║     {char4}     ║║           ║║         {number4} ║╚═══════════╝"),

        "num3_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num3_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num3_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),
        "num3_4": (f"╔═══════════╗║ {number4}         ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║         {number4} ║╚═══════════╝"),

        "num4_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num4_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num4_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),
        "num4_4": (f"╔═══════════╗║ {number4}         ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║         {number4} ║╚═══════════╝"),

        "num5_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num5_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num5_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),
        "num5_4": (f"╔═══════════╗║ {number4}         ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║         {number4} ║╚═══════════╝"),

        "num6_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num6_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num6_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),
        "num6_4": (f"╔═══════════╗║ {number4}         ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║         {number4} ║╚═══════════╝"),

        "num7_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num7_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num7_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),
        "num7_4": (f"╔═══════════╗║ {number4}         ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║         {number4} ║╚═══════════╝"),
        
        "num8_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num8_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num8_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),
        "num8_4": (f"╔═══════════╗║ {number4}         ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║         {number4} ║╚═══════════╝"),

        "num9_1": (f"╔═══════════╗║ {number1}         ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║         {number1} ║╚═══════════╝"),
        "num9_2": (f"╔═══════════╗║ {number2}         ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║         {number2} ║╚═══════════╝"),
        "num9_3": (f"╔═══════════╗║ {number3}         ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║         {number3} ║╚═══════════╝"),
        "num9_4": (f"╔═══════════╗║ {number4}         ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║         {number4} ║╚═══════════╝"),

        "num10_1": (f"╔═══════════╗║ {number1}        ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║     {char1}     ║║           ║║        {number1} ║╚═══════════╝"),
        "num10_2": (f"╔═══════════╗║ {number2}        ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║     {char2}     ║║           ║║        {number2} ║╚═══════════╝"),
        "num10_3": (f"╔═══════════╗║ {number3}        ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║     {char3}     ║║           ║║        {number3} ║╚═══════════╝"),
        "num10_4": (f"╔═══════════╗║ {number4}        ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║     {char4}     ║║           ║║        {number4} ║╚═══════════╝"),
        
        }
    
        print(f'{numberDict[f"{numKey1}"][0:13]}     {numberDict[f"{numKey2}"][0:13]}     {numberDict[f"{numKey3}"][0:13]}       {numberDict[f"{numKey4}"][0:13]}')
        print(f'{numberDict[f"{numKey1}"][13:26]}     {numberDict[f"{numKey2}"][13:26]}     {numberDict[f"{numKey3}"][13:26]}       {numberDict[f"{numKey4}"][13:26]}')
        print(f'{numberDict[f"{numKey1}"][26:39]}     {numberDict[f"{numKey2}"][26:39]}     {numberDict[f"{numKey3}"][26:39]}       {numberDict[f"{numKey4}"][26:39]}')
        print(f'{numberDict[f"{numKey1}"][39:52]}     {numberDict[f"{numKey2}"][39:52]}     {numberDict[f"{numKey3}"][39:52]}       {numberDict[f"{numKey4}"][39:52]}')
        print(f'{numberDict[f"{numKey1}"][52:65]}     {numberDict[f"{numKey2}"][52:65]}     {numberDict[f"{numKey3}"][52:65]}       {numberDict[f"{numKey4}"][52:65]}')
        print(f'{numberDict[f"{numKey1}"][65:78]}     {numberDict[f"{numKey2}"][65:78]}     {numberDict[f"{numKey3}"][65:78]}       {numberDict[f"{numKey4}"][65:78]}')
        print(f'{numberDict[f"{numKey1}"][78:91]}     {numberDict[f"{numKey2}"][78:91]}     {numberDict[f"{numKey3}"][78:91]}       {numberDict[f"{numKey4}"][78:91]}')
        print(f'{numberDict[f"{numKey1}"][91:104]}     {numberDict[f"{numKey2}"][91:104]}     {numberDict[f"{numKey3}"][91:104]}       {numberDict[f"{numKey4}"][91:104]}')
        print(f'{numberDict[f"{numKey1}"][104:117]}     {numberDict[f"{numKey2}"][104:117]}     {numberDict[f"{numKey3}"][104:117]}       {numberDict[f"{numKey4}"][104:117]}')
        print(f'{numberDict[f"{numKey1}"][117:130]}     {numberDict[f"{numKey2}"][117:130]}     {numberDict[f"{numKey3}"][117:130]}       {numberDict[f"{numKey4}"][117:130]}')
        print(f'{numberDict[f"{numKey1}"][130:143]}     {numberDict[f"{numKey2}"][130:143]}     {numberDict[f"{numKey3}"][130:143]}       {numberDict[f"{numKey4}"][130:143]}')
