import json


my_store =	{
	'money': 100,
	'items':	[
  	{
  		'name': 'apple',
  		'amount':	3,
  		'price': 5
  	},
  	{
    	'name':	'orange',
    	'amount':	1,
  		'price': 10
  	},
    {
      'name':	'banana',
			'amount':	0,
			'price':	3
    }
	]
}

def sell(store,	selling_list):
  	for items in selling_list:
				for i in store['items']:
  					if (items == i['name']):
  							if i['amount'] > 0:
  									print(f'Vật phẩm {items} còn hàng.')
  							else:
  								  print(f'Vật phẩm {items} đã hết.')

sell(my_store, ['orange', 'banana', 'apple'])
