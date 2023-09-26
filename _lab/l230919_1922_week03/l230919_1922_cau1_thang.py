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

def sell0(store, selling_list):
  for i in selling_list:
    for item in store['items']:
      if item['name'] == i:
        if item['amount']>0: print(f'{i:>6} conhang')
        else:                print(f'{i:>6} hethang')
        break

def sell(store, selling_list):
  for i in selling_list:
    try:
      amount = store['items_d'][i]['amount']
      price = store['items_d'][i]['price']
    except:
      amount = -1

    if amount > 0:   
      print(f'{i} conhang')

      '''
      - If item still exists in store, decrease the amount by 1. And increase the total money.      
      print Sell 1 :item. Total money: :money
      '''
      amount -=1
      store['money'] += price
      print(f'''sell 1 {i:>6}. Total money: {store['money']}''')
    elif amount < 0: 
      print(f'{i} khongtontai')
    else:            
      print(f'No more {i} to sell.')

sell(my_store_d, ['apple', 'banana', 'orange', 'grape'])
# sell(my_store_d, ['applexx'])  #NOTE xuly khi :i ko co