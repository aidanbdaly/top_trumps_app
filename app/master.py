import request_api
import deck_generate
import hand_assignment
import result_select
import request_filter

def run(input_category,input_players):

    #Requesting raw data from the API based on category selection.
    card_data_unfiltered = request_api.get(input_category)

    #Filtering entries that have attributes with unknown values. The attributes
    #are dependent on input_category.
    card_data = request_filter.filter(card_data_unfiltered,input_category)

    #Generating a 'deck' of indexes ready to be applied to card_data.
    deck = deck_generate.generate(card_data)

    #A list of the dictionaries of each active card is created and the deck
    #is updated.
    active_cards_unprocessed, new_deck = hand_assignment.create(
                                                            input_players,
                                                            deck,
                                                            card_data)
    deck == new_deck

    #A list of only the desirable attributes of each card is created, alongside
    #a list of just the attribute names.
    active_cards, category_attributes = hand_assignment.assign(
                                                            active_cards_unprocessed,
                                                            input_category,
                                                            input_players)

    #The active attribute and the result is chosen.
    active_attribute, result = result_select.select(
                                                category_attributes,
                                                active_cards)

    return active_cards, active_attribute, result
