"""
Given a list of things:
○ things = ['pen', 'ruler', 'wallet', 'phone']
○ Write a function return the string contains all items, seperate by comma (,), but the 'and' before the last item.
"""

#        =  0      1        2         3
#        =  0      1        len()-2   len()-1
danhsach = ['pen', 'ruler', 'wallet', 'phone']

# print(len(danhsach))

s=''
chiso_cuoi   = len(danhsach)-1
chiso_kecuoi = len(danhsach)-1 -1
for chiso,thanhvien in enumerate(danhsach):
  if chiso == chiso_kecuoi:
    s = s + f'{thanhvien} '
  elif chiso == chiso_cuoi:
    s = s + f'and {thanhvien}'
  else:
    s = s + f'{thanhvien}, '

# s = s.replace(', and ', ' and ')  # khongco , o truoc and

print(s)
