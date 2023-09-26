import sys
import re


n = input('Nhập số người\n> ')

regex   = r'\d+'  # r aka raw string
matched = re.findall(regex, n)
if not matched:
  print('ERROR Vuilong nhap so')
  sys.exit(0)

n = int(n)
print(n)
