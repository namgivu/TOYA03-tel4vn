import json


my_store = {
  'money': 100,
  'items': [
    {
      'name': 'apple',
      'amount': 3,
      'price': 5
    },
    {
      'name': 'orange',
      'amount': 1,
      'price': 10
    }
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

 def sell(store, sell_list):
  
  for i in sell_list:
    try:
      amount = store['items_d'][i]['amount']
      price = store['items_d'][i]['price']
    except:
      amount = -1

      
    if amount > 0:
        # print(f'{i:>6} conhang')
        '''
        - if item still exits ...
        '''
        
        store['items_d'][i]['amount'] -= 1
        store['money'] += price
        print(f'''sell 1 {i:>6}. Total money: {store['money']}''')
    elif amount < 0: 
      print(f'{i:>6} khongtontai')
    else: 
      print(f'No more {i} to sell.')

print(json.dumps(my_store, indent=2))

sell(my_store, ['apple','banana','orange'])
