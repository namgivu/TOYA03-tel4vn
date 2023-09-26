a0 = ['dog', '0', 'cat', '2', 'elephant', '1']

a = [*a0]  # copy list :a0 to a new cloned one :a

print('--- a.sort()')
print(f'before sort  {a=}')
a.sort()  # reverse=False
print(f'after sort   {a=}')
a.sort(reverse=True)
print(f'after sort r {a=}')


print('\n--- b=sorted(a)')
a = [*a0]  # copy list :a0 to a new cloned one :a
print(f'before sort        {a=}')

a_sorted = sorted(a)  # reverse=False
print(f'after sort          {a=}')
print(f'after sort   {a_sorted=}')
a_sorted = sorted(a, reverse=True)
print(f'after sort r {a_sorted=}')


print('\n--- b=sorted(a, lambda i: xxx)')
member = [
  # 0 name        1 year
  ('Thanh',       1982),
  ('Nam',         1982),
  ('Han',         2016),
  ('Oppenheimer', 1904),
]
print(f'before sort         {member=}')
print(f'after sort  {sorted(member)=}')

sorted_member = sorted(member, key = lambda i: i[1])
print(f'after sort   {sorted_member=}')
