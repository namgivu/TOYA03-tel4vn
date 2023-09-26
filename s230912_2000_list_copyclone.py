a = ['dog', '0', 'cat', '2', 'elephant', '1']

a_copy0 = [*a]
a_copy0[0]='xx'; print(f'      {a=} \n{a_copy0=}')

print('\n---\n')

a_copy1 = a.copy()
a_copy1[1]='xx'; print(f'      {a=} \n{a_copy1=}')
