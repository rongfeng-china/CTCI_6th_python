import random
def shuffle(cards):
    n = len(cards)
    for i in range(n):
        index = random.randint(0,i)
        temp = cards[index]
        cards[index]=cards[i]
        cards[i] = temp
    return cards
    
cards = [1, 9, 3, 10, 7, 2, 7, 8, 9]
shuffle(cards)
print cards
