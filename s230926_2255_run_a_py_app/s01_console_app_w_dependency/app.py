import requests
import json

res = requests.get('https://api.upcitemdb.com/prod/trial/lookup?upc=190199267961')
print(f'{res.status_code=}')
print(f'{json.dumps(res.json(), indent=2)}')
