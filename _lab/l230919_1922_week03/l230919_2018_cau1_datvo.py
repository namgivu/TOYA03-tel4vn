import json

my_store = {
  'money': 100,
  
  'items': {'apple': {
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


def sell(store, selling_list):
  for item in selling_list:
    if item not in store['items_d']:
      print(f"{item} khong ton tai")
    else:  # cotontai
      if store['items_d'][item]['amount'] > 0:
        store['items_d'][item]['amount'] -= 1
        store['money'] += store['items_d'][item]['price']
        print(f"Sale 1 {item}. Total money: {store['money']}")
      else:
        print(f"No more {item} to sell.")


sell(my_store, ['apple', 'orange', 'orange', 'banana'])
