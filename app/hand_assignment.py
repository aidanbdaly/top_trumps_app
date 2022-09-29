import attributes

#This function takes the result from deck_generate along with the selected
#player count to create a list of the dictionaries of the cards that are
#currently in play.

def create(
        input_player_count, input_deck,
        input_card_data):

    active_cards = []
    player_list = list(range(int(input_player_count)))

    for player in player_list:

        #Here we take the last item (the top of the deck) in the list of
        #indexes and apply it to the list of dictionaries.
        top_card = input_deck[-1]
        #The corresponding dictionary is appended to active_cards.
        active_cards.append(input_card_data[top_card])
        #Moving the top card to the bottom of the deck.
        input_deck.insert(0, input_deck[-1])
        del input_deck[-1]

    return active_cards, input_deck


def assign(input_active_cards, category_type, input_player_count):

    #Creating empty list for each player. These will hold the desirable
    #attribute-value pairs.
    card_data_assigned = [[] for _ in range(int(input_player_count))]
    category_attributes = attributes.categories[category_type]

    #Appending desirable attribute-value pairs to card_data_assigned.
    for count, item in enumerate(input_active_cards):

        for attribute in category_attributes:
            #Pulling desirable data from input_active_cards
            card_data_assigned[count].append([attribute, item[attribute]])

    #Special case for 'people': the attribute value for 'vehicles' and
    #'starships'returns a list of links to each individual API entry. So we
    #take the len() instead to get the total of each.
    for card in card_data_assigned:

        for attribute in card:

            if attribute[0] in ['vehicles','starships']:
                attribute[1] = len(attribute[1])

    ## NOTE: card_data_assigned now represents the final form of the card
    return card_data_assigned, category_attributes
