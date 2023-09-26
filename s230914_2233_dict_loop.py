d = {
  'a':122,
  'b':333,
}

print('\n--- in d\n')
for i in d:
  print(i)

print('\n--- in d.keys()\n')
for k in d.keys():
  print(k)

print('\n--- in d.values()\n')
for v in d.values():
  print(v)

print('\n--- in d.items()\n')
for k,v in d.items():
  print(f'{k=} {v=}')
