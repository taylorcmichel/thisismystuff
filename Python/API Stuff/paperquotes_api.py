# This script operates on a tokenized API that I found via YouTube that
# allows you to submit GET requests to pull famous quotes based on a
# variety of conditions, of which I used number of quotes to pull.
# 
# https://api.paperquotes.com/
#
# The intent of this script is to:
# 1. Create an empty 'results_lst' to store a dictionary/JSON of queried
#    quotes later in the script
# 1. Query data dynamically from the API based upon a number of quotes
# 2. Submit the header and TOKEN as authorization for access
# 3. Build a new dictionary/JSON object based upon the 'results' portion
#    of the API JSON object
# 5. Append the results of each query to the pre-created 'results_lst'
#    one at a time
# 6. Print each new queried quote to the terminal one at at time QC the
#    script as it proceeds
# 6. Write all queried quotes to a new local JSON file using json.dump 
# 
# This new JSON file will isolate a core of information that we can that
# we can further focus on if need be. Probably need to, if anything is
# to be done on the client side. The default formatting of the JSON on
# the server side is atrocious.

import json
import requests

#Create empty 'results_lst' for dictionary/JSON storage later in the
#script
results_lst = []

#Loop the core code x-number of times
for count in range(20):

    #The API link will loop dynamically as per the f-string
    link = f'https://api.paperquotes.com/apiv1/quotes/?lang=en&limit={count}'

    #TOKEN authorization direct from paperquotes
    res = requests.get(link, headers={'Authorization': 'TOKEN a83459a8ea7585c8694319b9cbff3d954ec2c0ad'}).json()

    #Building the extracts from the API JSON
    for r in res['results']:
        quote =  r['quote']
        author = r['author']
        language = r['language']

    #Build the new dictionary/JSON object on the client side
    new_data = {
        'quote': quote,
        'author': author,
        'language': language
    }

    #Append the new dictionary/JSON object to the 'results_lst' list
    #created earlier one-by-one
    results_lst.append(new_data)

    #Print each queried quote to the screen one-by-one for QC purposes
    print(new_data['quote'] + '\n')

#After building the complete client-side dictionary/JSON 'results_lst',
#write it to the client-side JSON file for later use
with open('paperquotesapi.json', 'w') as f:
    json.dump(results_lst, f, indent=2)
