
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

print('Xin chao. Moi ban chon mat hang ^^')

for i in my_store_d['items']:
  print(f"{i['name']:<6} ${i['price']}")

print('\n---\n')

for k,v in my_store_d['items_d'].items():
  # print(f'{k=:<6} {v=} ')
  print(f'''{k:<6} ${v['price']} ''')
