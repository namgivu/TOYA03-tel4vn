import json


my_store_d = {
  'money': 100,

  'items': [
    {
      'name'  : 'apple',
      'amount': 3,
      'price' : 5,
    },
    {
      'name'  : 'orange',
      'amount': 1,
      'price' : 10,
    },
    {
      'name'  : 'banana',
      'amount': 0,
      'price' : 3,
    },
  ],
}

'''
yeucau tao 
  'items_d': {
    'apple': {
      'amount': 3,
      'price' : 5,
    },
    'orange': {
      'amount': 1,
      'price' : 10,
    },
    'banana': {
      'amount': 0,
      'price' : 3,
    },
  }
'''

#region step 1

# items_d = []  # list danhsach mang
items_d   = {}  # dict rong

#endregion step 1


#region step 2
'''
items_d = {
  k      : {}  # name 
  apple  : {},
  orange : {},
  banana : {},
} 
'''
for i in my_store_d['items']:
  k          = i['name']
  items_d[k] = {}
#endregion step 2


#region step 3
'''
items_d = {
  #      :  1      2
  apple  : {price, amount},
  orange : {price, amount},
  banana : {price, amount},
} 
'''
for i in my_store_d['items']:
  name   = i['name']
  price  = i['price']
  amount = i['amount']

  #          {} [key]      = value
  items_d[name] ['price']  = price
  items_d[name] ['amount'] = amount
#endregion step 3

print(items_d)
print(json.dumps(items_d, indent=2))
