print('--- list reference')
a1 = ['dog', 'cat', 'elephant', 'mouse']
a2 = a1  # reference only, not value replicated
print(f'{a1=}')
print(f'{a2=}')

print()

a1[0] = 'newdog'
print(f'{a1=}')
print(f'{a2=}')


print()

a2[2] = 'newelephant'
print(f'{a1=}')
print(f'{a2=}')

print('--- replicate list')

a1 = ['dog', 'cat', 'elephant', 'mouse']
a2 = [i for i in a1]  # list replicate
a1[0] = 'newdog' ; print(f'{a1=}') ; print(f'{a2=}')  # a1 updated ; a2 untouched

a1 = ['dog', 'cat', 'elephant', 'mouse']
a2 = [ *a1 ]  # list replicate 2nd  # replace *a1 by its value w/ comma separated
a1[0] = 'newdog' ; print(f'{a1=}') ; print(f'{a2=}')  # a1 updated ; a2 untouched
