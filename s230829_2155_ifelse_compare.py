"""
#                        -1    0    1
compare(i1, i2) -> -1 if i1 <  i2
                    0 if i1 == i2
                    1 if       i2 < i1
"""

def compare(i1, i2):
  if i1 < i2:
    return -1
  if i1 == i2:
    return 0
  if i1 > i2:
    return 1

print( compare(1,   22) )
print( compare(22,  22) )
print( compare(333, 22) )

print('\n### v2\n')

def compare_v2(i1, i2):
  if i1 < i2:
    r = -1
  else:
    if i1 == i2:
      r = 0
    else:
      if i1 > i2:
        r = 1

  return r

print( compare_v2(1,   22) )
print( compare_v2(22,  22) )
print( compare_v2(333, 22) )

print('\n### v3\n')

def compare_v3(i1, i2):
  if i1 < i2:
    r = -1
  elif i1 == i2:
    r = 0
  elif i1 > i2:
    r = 1

  return r

print( compare_v3(1,   22) )
print( compare_v3(22,  22) )
print( compare_v3(333, 22) )

print('\n### v3\n')

def compare_v4(i1, i2):
  if i1 < i2:
    r = -1
  elif i1 == i2:
    r = 0
  else:  # ie i1 > i2
    r = 1

  return r

print( compare_v4(1,   22) )
print( compare_v4(22,  22) )
print( compare_v4(333, 22) )
