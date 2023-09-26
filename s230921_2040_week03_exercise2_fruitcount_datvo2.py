parties = {
  'Person_A': {
    'apple': 5,
    'orange': 2
  },
  'Person_B': {
    'cherry': 3,
    'orange': 1
  },
  'Person_C': {
    'grape': 10,
    'mango': 6
  }
}

total = {}

for fruit_d in parties.values():
  for fruit, count in fruit_d.items():
    if fruit in total:
      total[fruit] += count
    else:
      total[fruit] = count

print(total)
