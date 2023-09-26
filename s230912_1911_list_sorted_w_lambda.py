a0 = ['dog', 'cat', 'elephant']

a = [*a0]
print(a)

a = [*a0] ; a.sort()
print(a)

a = [*a0] ; a.sort(reverse=True)
print(a)

print('---')
member0 = [
  # 0             1
  ('Thanh',       1982),
  ('Nam',         1982),
  ('Han',         2016),
  ('Oppenheimer', 1904),
]

m = [*member0]
print(m)

m = [*member0] ; m.sort()
print(m)
m = [*member0] ; m.sort(reverse=True)
print(m)

# sort by :year
m = sorted(member0, key=lambda i: i[1])
print(f'{member0=}')
print(f'{m=}')

# sort by :year reversed
m = sorted(member0, key=lambda i: i[1], reverse=True)
print(f'{member0=}')
print(f'{m=}')

# sort by :year then :name  ie 1982Nam 1982Thanh is the sorted order
m = sorted(member0, key=lambda i: f'{i[1]}{i[0]}')
print(f'{member0=}')
print(f'{m=}')
