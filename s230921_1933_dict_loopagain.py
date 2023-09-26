d = {
  'a': 122,
  'b': 333,
}
print(f'{d=}')

print('\n--- loop for in ie default loop key\n')
for i in d:
  print(i)
print('.')
for i in d.keys():
  print(i)

print('\n--- loop value\n')

for i in d.values():
  print(i)

print('\n--- loop key:value\n')
for k,v in d.items():
  print(f'{k=} {v=}')
