"""
max_2num(i1, i2)
"""
def max_2num(i1, i2):
  if i1>i2: return i1
  else:     return i2

# print( max_2num(i1=1, i2=22) )
# print( max_2num(i1=4444, i2=333) )

i1=1;    i2=22  ; print( f'max of {i1:<4} and {i2:<4} is {max_2num(i1,i2)}' )
i1=4444; i2=333 ; print( f'max of {i1:<4} and {i2:<4} is {max_2num(i1,i2)}' )
