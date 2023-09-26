#region demo list/dict assignment is ref assign
l  = [1, 22]
l2 = l
print(f'{l=}')
print(f'{l2=}')
l.append(333)  # also effect l2 -> l2 = l is ref assign
print(f'{l=}')
print(f'{l2=}')


print('\n---\n')
d  = {'a': 122}
d2 = d

print(f'{d=}')
print(f'{d2=}')
d['a'] = 333  # also effect d2 -> d2 = d is ref assign
print(f'{d=}')
print(f'{d2=}')


print('\n---\n')
s = 'abb'
t = s

print(f'{s=}')
print(f'{t=}')
s = 'ccc'  #NOTE NOT effect t -> t = s is value assign
print(f'{s=}')
print(f'{t=}')

#endregion demo list/dict assignment is ref assign

#region copy list/dict
print('\n---\n')
l  = [1, 22]
l2 = l.copy()
l3 = [*l]

print(f'{l=}')
print(f'{l2=}')
print(f'{l3=}')
l.append(333)
print(f'{l=}')
print(f'{l2=}')
print(f'{l3=}')


print('\n---\n')
d  = {'a': 122}
d2 = d.copy()
d3 = {**d}

print(f'{d=}')
print(f'{d2=}')
print(f'{d3=}')
d['a'] = 333
print(f'{d=}')
print(f'{d2=}')
print(f'{d3=}')
#endregion copy list/dict
