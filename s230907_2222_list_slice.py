animals = ['dog', 'cat', 'elephant', 'mouse']
#       =  0      1      2           3
#       =  -4     -3     -2          -1
#       =  len-4  len-3  len-2       len-1

print(animals)
print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])
# print(animals[4])  # IndexError: list index out of range

print()

print(animals[-1])
print(animals[-2])

print()

print(f'{animals[ 0]=}')
print(f'{animals[ 1]=}')
print(f'{animals[-1]=}')
print(f'{animals[-2]=}')

print()
print(f'{animals[     -1 ]=}')
#               [     -1 ]
#               [len()-1 ]
print(f'{animals[-2+1]=}')


print()

#          start_at:end_at
#          start_at:end_at_incl + 1
print(f'{animals[ 0:1  ]=}')
print(f'{animals[ 0:0+1]=}')
print(f'{animals[ 0:2  ]=}')
print(f'{animals[ 0:1+1]=}')

print()

print(f'{animals[ 1:3]=}')
print(f'{animals[ 1:2+1]=}')

print()

#                 :1
#        default=0:1
print(f'{animals[ :1  ]=}')
print(f'{animals[0:1  ]=}')
print(f'{animals[0:0+1]=}')
print(f'{animals[0:2+1]=}')

print()

print( f'{animals[ :-1      ]=}')
print( f'{animals[0:-1      ]=}')
#print(f'{animals[0:len-1   ]=}')
#print(f'{animals[0:len-2 +1]=}')

print()

#                0:
#                0:default=len()
print(f'{animals[0:  ]=}')
print(f'{animals[1:  ]=}')
