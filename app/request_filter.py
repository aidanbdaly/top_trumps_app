import attributes


def filter(
        input_card_data,
        category_type):

    request_result_filtered = []

    #Some entries contain unusable attribute values. These would make
    #unplayable cards and are thus removed.
    for entry in input_card_data:
        #Cumalitive count of unwanted.
        total_unwanted = 0

        for attribute in entry:

            #Checking if the attribute in question is in the list of selected
            #attributes for the card.
            if attribute in attributes.categories[category_type]:

                if entry[attribute] == 'unknown':
                    total_unwanted += 1

                if ',' in entry[attribute]:
                    total_unwanted += 1

                if 'n/a' in entry[attribute]:
                    total_unwanted += 1

        if total_unwanted == 0:
            request_result_filtered.append(entry)

    return request_result_filtered
