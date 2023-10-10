def hi(*args):
  # return f'Hi {args}'

  if not args:
    return 'Hi!'

  if len(args)>1:
    namestr = ', '.join(args[0:-1])
    namestr = f'{namestr}, and {args[-1]}'
    return   f"Hi {namestr}!"
  elif len(args)==1:
    name = args[0]
    if name:
      return f'Hi {name}!'
    else:
      return f'Hi!'

print( hi()                      )
print( hi('Mom')                 )
print( hi('Mom', 'Dad')          )
print( hi('1',   '22', '333')    )
print( hi('A',   'B',  'C', 'D') )
