import json
import time
from urllib.request import urlopen

results_lst = []

for count in range(5):
    with urlopen(f'https://rickandmortyapi.com/api/character/?page={count}') as response:
        source = response.read()

    data = json.loads(source)

    for res in data['results']:
        name = res['name']
        status = res['status']
        species = res['species']
        origin_name = res['origin']['name']
        print(name,',',status,',',species,',',origin_name)

        new_data = {
            'name':name,
            'status':status,
            'species':species,
            'origin_name':origin_name
        }
    
        results_lst.append(new_data)

    time.sleep(3)

print(results_lst)

with open('rickandmortyapi.json', 'w') as f:
    json.dump(results_lst, f, indent=2)
