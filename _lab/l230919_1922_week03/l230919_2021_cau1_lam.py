

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
}

def sell(store, selling_list):
  print(json.dumps(my_store_d), indent=2)
  for i in selling_list:
    if my_store_d['items_d'][i]['amount'] > 0: 
      print(f'{my_store_d['items_d']} conhang')
    else: 
      print(f'{my_store_d['items_d']} hethang')
     
sell(my_store, ['apple', 'banana'])
