import requests
import json


def get(category):

    request_result_list = []
    address_base = "https://swapi.dev/api/"
    page = 1

    #A while loop is created to send requests for each page of data.
    while True:
        #creating the address string
        address_categorised = (address_base
                              + category
                              + '?page='
                              + str(page))
        #Sending API request.
        response = requests.get(address_categorised)
        #Converting to readable object.
        response_unpacked = response.json()
        #Accessing JSON attribute 'next' that specifies the next page address.
        page_next = response_unpacked['next']

        #Since NULL value is returned if the last page is reached, we check for
        #type None.
        if page_next is None:
            request_result_list.append(response_unpacked['results'])
            break
        else:
            page += 1
            request_result_list.append(response_unpacked['results'])
            continue

    #Concatenating all pages of data into one list.
    request_result = []
    list(map(request_result.extend, request_result_list))

    return request_result
