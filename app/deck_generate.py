import random

#This function generates a list of randomly assorted indexes equal to the
#number of playable cards in the deck.
def generate(input_card_data):

    #Checking if the total playable cards is less than the max deck size of 32.
    total_cards = len(input_card_data)

    if total_cards < 32:
        #If it is, reduce the max deck size.
        deck_upperlimit = total_cards

    else:
        deck_upperlimit = 32

    #Calculate total cards in deck.
    deck_count = random.randint(24,deck_upperlimit)
    deck = list(range(deck_count))
    #Shuffling the deck.
    random.shuffle(deck)

    return deck
