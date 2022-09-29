import random


def select(
        category_attributes,
        input_active_cards):

    #The deciding attribute is randomly selected.
    random_index = random.randint(1,(len(category_attributes) - 1))
    deciding_attribute = category_attributes[random_index]
    #All active deciding attribute values:
    active_attribute_values = []

    for card in input_active_cards:

        for attribute in card:
            #Attribute[0] represents the name of the attribute.
            #Attribute has form ['AttributeName','Value']

            if attribute[0] == deciding_attribute:
                active_attribute_values.append(float(attribute[1]))

    #The victor is the max value from the list.
    victor_value = max(active_attribute_values)
    #Checking if there are multiple players with max value
    victor_value_count = active_attribute_values.count(victor_value)

    #Creating HTML string. 1 is added since index of 0 represents player 1's
    #attribute value.
    if victor_value_count == 1:

        outcome = ('Player '
                  + str(active_attribute_values.index(victor_value)
                  + 1))

    #Runs true if max value instance is not unique.
    else:

        outcome = 'Draw!'

    return  deciding_attribute, outcome
