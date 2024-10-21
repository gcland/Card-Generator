class Player:
    def __init__(self, playerName, position, cards):
        self.playerName = playerName
        self.position = position
        self.cards = cards

    def get_playerName(self):
        return self.playerName
    
    def receive_card(self, suit, num):
        # self.cards[f'{num}'] = f'{suit}'
        if suit == "club":
            char = "♣"
        elif suit == "diamond":
            char = "♦"
        elif suit == "heart":
            char = "♥"
        elif suit == "spade":
            char = "♠"
        cardStr = f'{num}{char}'
        self.cards.append(cardStr)
        

    def get_cards(self):
        # print(self.cards)
        return self.cards