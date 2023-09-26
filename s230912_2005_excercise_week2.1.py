"""
Given a list of things:
○ things = ['pen', 'ruler', 'wallet', 'phone']
○ Write a function return the string contains all items, seperate by comma (,), but the 'and' before the last item.
"""
things = ['pen', 'ruler', 'wallet', 'phone']

s = ''
for idx,i in enumerate(things):
  if idx < len(things)-1:
    s   = s + f'{i}, '
  else:
    s   = s + f'and {i}'

s = s.replace(', and', ' and')  # no comma , before :and

print(s)
