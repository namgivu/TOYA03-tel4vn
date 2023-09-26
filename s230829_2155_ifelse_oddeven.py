"""
is_odd(i)
  is_even(i)
"""

print('\n### odd\n')

def is_odd(i):
  if i % 2 == 1:
    r = True
  else:
    r = False

  print(f'{i:<3} is odd? {r}')

is_odd(i=1)
is_odd(i=22)
is_odd(i=333)

print('\n### even\n')

def is_even(i):
  if i % 2 == 0:
    r = True
  else:
    r = False

  print(f'{i:<3} is even? {r}')

is_even(i=1)
is_even(i=22)
is_even(i=333)
