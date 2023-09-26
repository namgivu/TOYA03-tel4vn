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

def sell(store, selling_list) :
  for i in selling_list:
    try:
      amount = store['items_d'][i]['amount']
    except:
      amount = -1
      
    if amount > 0:
      print(f'{i} con hang')
      store['items_d'][i]['amount'] -= 1
      store['money'] += store['items_d'][i]['price']
      print(f"Sell 1 {i}. Total money: {store['money']}.")
    
    elif amount < 0:
      print(f'{i}  khong ban')
    
    else:
      print(f'No more {i} to sell')

sell(my_store_d, ['apple', 'orange', 'banana', 'chomchom'])