d = {'a':122, 'b':333}
print(f'{d=}')
d.pop('b')
print(f'{d=}')
# d.pop('b')      #NOTE key 'b' nomore exist -> raise error
d.pop('b', None)  # no error if key 'b' not there
print(f'{d=}')

a_value = d.pop('a', None)
print(f'{a_value=}')
print(f'{d=}')
