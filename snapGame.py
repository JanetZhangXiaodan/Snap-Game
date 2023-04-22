import random

def shuffledCards(numPacks):
    SUITS = ['S','H','D','C']
    FACEVALUE = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [facevalue + suit for suit in SUITS for facevalue in FACEVALUE] * int(numPacks)
    random.shuffle(deck)
    return deck

def snapGamePlay(numPacks, matchCondition):
    deck = shuffledCards(int(numPacks))
    playerOneCards = []
    playerTwoCards = []
    commonDiscardPile = []

    for card in deck:
        commonDiscardPile.append(card)
        if len(commonDiscardPile) < 2:
            continue

        if matchCondition == 'suit' and commonDiscardPile[-1][-1] == commonDiscardPile[-2][-1]:
            snap_winner = random.choice(['Player 1', 'Player 2'])
            if snap_winner == 'Player 1':
                playerOneCards += commonDiscardPile
            else:
                playerTwoCards += commonDiscardPile
            commonDiscardPile = []
        elif matchCondition == 'value' and commonDiscardPile[-1][:-1] == commonDiscardPile[-2][:-1]:
            snap_winner = random.choice(['Player 1', 'Player 2'])
            if snap_winner == 'Player 1':
                playerOneCards += commonDiscardPile
            else:
                playerTwoCards += commonDiscardPile
            commonDiscardPile = []
        elif matchCondition == 'both' and commonDiscardPile[-1] == commonDiscardPile[-2]:
            snap_winner = random.choice(['Player 1', 'Player 2'])
            if snap_winner == 'Player 1':
                playerOneCards += commonDiscardPile
            else:
                playerTwoCards += commonDiscardPile
            commonDiscardPile = []
    winner = declareWinner(playerOneCards, playerTwoCards)

def declareWinner(playerOneCards, playerTwoCards):
    print(f"Player 1 has {len(playerOneCards)} cards.")
    print(f"Player 2 has {len(playerTwoCards)} cards.")
    if len(playerOneCards) > len(playerTwoCards):
        print("Player 1 wins!")
    elif len(playerOneCards) < len(playerTwoCards):
        print("Player 2 wins!")
    else:
        print("Draw!")
        
if __name__ == '__main__':

    packChoice = ['1','2','3','4','5']
    conditionChoice = ['suit','value','both']

    while True:
        num = input('Input Int: How many packs of cards to use? (1-5 packs)')
        choice = input('Input Str: suit, value, both')
        
        if num not in packChoice or choice not in conditionChoice:
            print('Try again.')
        else:
            break

    snapGamePlay(num, choice)