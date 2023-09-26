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
  ]
}

def sell(store, selling_list):
  print(json.dumps(store, indent=2))
  for item in selling_list:
    print(item)
  
  store["items"][len(store["items"])] = {'name':'banana','amount': 0,'price': 3}


#print(json.dumps(my_store, indent=2))
sell(my_store, [])
