import attributes


def filter(
        input_card_data,
        category_type):

    request_result_filtered = []

    #Some entries contain the attribute values 'unknown'. These would make
    #unplayable cards and are thus removed.
    for entry in input_card_data:
        #Cumalitive count of unknowns.
        total_unknowns = 0

        for attribute in entry:

            #Checking if the attribute in question is in the list of selected
            #attributes for the card.
            if attribute in attributes.categories[category_type]:

                if entry[attribute] == 'unknown':
                    total_unknowns += 1

        if total_unknowns == 0:
            request_result_filtered.append(entry)

    return request_result_filtered
