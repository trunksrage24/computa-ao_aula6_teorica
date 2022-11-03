"""
14 cartas num baralho
1 a 10, j, q, k, a
2 baralhos, 1p e comp
1 - representar cada deck
2 - baralhar decks
3 - print decks
4 - go fish: print last 2 cards
5 - compare: 
"""

import random

#valores dentro do baralho
values = list(range(1,14))
valuesC = values.copy()

#funçao shuffel - baralha o deck
def shuffleDeck(deckshuffle):
    random.shuffle(deckshuffle)

#funçao deck - assume listas de fora da funçao
def printDeck(deck):
    auxdeck = []
    for num in deck:
        auxdeck.append(CodifyCard(num))
    return str(auxdeck)

#atribui valor as carta especiais
def CodifyCard(valuecard):
    if valuecard == 11:
        return "J"
    elif valuecard == 12:
        return "Q"
    elif valuecard == 13:
        return "K"
    elif valuecard == 14:
        return "A"
    else: 
        return str(valuecard)

#mostrar hand e discard cartas
def Hand(mydeck):
    playerhand = mydeck[:-3:-1]
    return playerhand

#imprimir decks antes de baralhar
print("player deck unshuffled " + printDeck(values))
print("")
print("computer deck unshuffled " + printDeck(valuesC))

#baralhar ambos os decks
shuffleDeck(values)
shuffleDeck(valuesC)

#imprimir os decks baralhados
print("player deck " +  printDeck(values))
print("")
print("computer deck " + printDeck(valuesC))

playerhand = Hand(values)
comphand = Hand(valuesC)

#imprimir 2 ultimas cartas baralhadas
print("last 2 cards shuffled for player" + str(playerhand))
print("")
print("last 2 cards shuffled for computer" + str(comphand))

