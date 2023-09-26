"""
ip00 httpcode00
ip01 httpcode00
ip02 httpcode00
ip03 httpcode00

ip10 httpcode10
ip11 httpcode10
ip12 httpcode10
ip13 httpcode10

count ip for each httpcodeXX

--- thinking
cook ip_c_d = {
  httpcodeXX : count_ip
}
"""
d = {
  'a':122,
  'b':333,
}
print('a' in d)      # True
print('b' in d)      # True

print('c' in d)      # False
print('c' not in d)  # True


# import sys; sys.exit()
print('\n---\n')

INP = '''
ip00 httpcode00
ip01 httpcode00
ip02 httpcode00
ip03 httpcode00

ip10 httpcode10
ip11 httpcode10
ip12 httpcode10
ip13 httpcode10
'''.strip()
INP = INP.split('\n')
INP = [i for i in INP  if i]
INP = [i.split(' ') for i in INP]
print(INP)

count_d = {}  # aka {httpcode:ip_count} dict
for i in INP:
  # print(i)
  ip       = i[0]
  httpcode = i[1]
  print(f'{ip=:<3} {httpcode=:<3}')

  if   httpcode not in count_d: count_d[httpcode]  = 1
  elif httpcode     in count_d: count_d[httpcode] += 1
print(count_d)
