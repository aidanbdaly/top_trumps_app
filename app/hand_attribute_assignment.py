
def assign(input_active_cards, category_type, input_player_count):

    #this is a dictionary that specifies the chosen attributes for each card type. For simplicity they are not dynamic
    categories = {
        'people': ['name','height','mass','vehicles','starships'],
        'vehicles': ['name','length','max_atmosphering_speed','crew','passengers'],
        'starships': ['name','hyperdrive_rating','max_atmosphering_speed','cargo_capacity','passengers'],
        'planets': ['name','rotation_period','orbital_period','diameter','surface_water']
                 }

    #Creating empty list for each player. These will hold the desirable attribute-value pairs
    card_data_assigned = [[] for _ in range(int(input_player_count))]

    category_attributes = categories[category_type]

    #Appending desirable attribute-value pairs to card_data_assigned
    for count, item in enumerate(input_active_cards):
        for attribute in category_attributes:
            #Pulling desirable data from input_active_cards
            card_data_assigned[count].append([attribute, item[attribute]])


    ## NOTE: card_data_assigned now represents the final form of the card
    return card_data_assigned, category_attributes
