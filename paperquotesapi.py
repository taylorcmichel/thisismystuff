import json
import requests

results_lst = []

for count in range(5):
    link = f'https://api.paperquotes.com/apiv1/quotes/?lang=en&limit={count}'

    res = requests.get(link, headers={'Authorization': 'TOKEN a83459a8ea7585c8694319b9cbff3d954ec2c0ad'}).json()

    for r in res['results']:
        quote =  r['quote']
        author = r['author']
        likes = r['language']

    new_data = {
        'quote': quote,
        'author': author,
        'likes': likes
    }

    results_lst.append(new_data)

    # data = json.dumps(res, indent=2)

print(results_lst)

with open('paperquotesapi.json', 'w') as f:
    json.dump(results_lst, f, indent=2)