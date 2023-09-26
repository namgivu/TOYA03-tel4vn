import requests  # pip install requests

#   =          method url/address
res = requests.get(   'https://api.upcitemdb.com/prod/trial/lookup?upc=190199267961')

print(f'{res=}')

# print(f'{res.__dict__=}')

# ref pycharm debug
print(f'{res.status_code=:<}')
print(f'{res.headers}=')
print(res.text)

d = res.json()
print(d)
print(len(d['items']))
print(    d['items'] )
