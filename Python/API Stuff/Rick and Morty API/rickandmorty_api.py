# This script operates on an open API that I found online for the popular
# show Rick and Morty. Information can be found at the website below:
# 
# https://rickandmortyapi.com/
#
# The intent of this script is to:
# 1. Query data dynamically from the API based upon a number of pages
# 2. Build a new JSON object based upon the structure of API data
# 3. Write the queried data to a new local JSON file for later analysis
# 
# This new JSON file will isolate a core of information from the greater
# raw dataset that we can that we can further focus on if need be.

import json
import time
from urllib.request import urlopen

#Create an empty list that we will append each new dictionary/JSON
#object into at the end of each loop below
results_lst = []

#Begin the loop, go to the APIs URL {appropriate page} and load the
#content of that page (a JSON string) into a variable called 'source'
#for each iteration
for count in range(5):
    with urlopen(f'https://rickandmortyapi.com/api/character/?page={count}') as response:
        source = response.read()

    #Parse the resulting JSON string from above and convert it into
    #a Python dictionary
    data = json.loads(source)

    #Extract the necessary information from the API and print it
    #line-by-line to QC it, ensuring that this is, indeed, what
    #what we want
    for res in data['results']:
        name = res['name']
        status = res['status']
        species = res['species']
        origin_name = res['origin']['name']
        print(name,',',status,',',species,',',origin_name)

        #Build a new dictionary that will be the basis for the
        #local JSON file
        new_data = {
            'name':name,
            'status':status,
            'species':species,
            'origin_name':origin_name
        }
    
        #Add the new dictionary/JSON object created just above
        #to the 'results_lst' list created before the loop
        results_lst.append(new_data)
    
    #Artificial delay so as to not upset the hosts of the API
    time.sleep(3)

#Write 'results_lst' to a new local JSON object for further
#analysis later
with open('rickandmortyapi.json', 'w') as f:
    json.dump(results_lst, f, indent=2)
