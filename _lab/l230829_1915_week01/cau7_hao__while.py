def tong(n):
  i = 1
  s = 0
  while i <= n:
    s = s + i
    i = i + 1
  print(f'Tổng từ 1 đến a là: {s}')

n = int(input('Nhập số bạn muốn: \n'))
tong(n)
