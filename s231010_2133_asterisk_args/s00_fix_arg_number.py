def hi(name=''):
  if name:               # ie if name has-value:
    return f'Hi {name}!'
  elif not name:         # ie elif not-has-value name:
    return f'Hi!'

print( hi('Mom')      )
print( hi(name='Dad') )
print( hi() )
