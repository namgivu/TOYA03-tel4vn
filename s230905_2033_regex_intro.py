import re

print('---')
s = '122'
m = re.findall('122', s)

if m: print(True)
else: print(False)
# print(True if m else False)

print('---')
m = re.findall('122.*', '122') ; print(True if m else False)
m = re.findall('122.*', '122 333') ; print(True if m else False)

print('--- namsinh 193x 200x 201x 202x')
m = re.findall('(193|200|201|202)\d', '1890') ; print(True if m else False)
m = re.findall('(193|200|201|202)\d', '1930') ; print(True if m else False)
m = re.findall('(193|200|201|202)\d', '2000') ; print(True if m else False)
m = re.findall('(193|200|201|202)\d', '2020') ; print(True if m else False)
m = re.findall('(193|200|201|202)\d', '202c') ; print(True if m else False)

print('--- ngaythang DD/MM/YYYY')
m = re.findall('\d\d/\d\d/\d\d\d\d', '05/09/2023') ; print(True if m else False)
m = re.findall('\d\d/\d\d/\d\d\d\d', '05/22/2023') ; print(True if m else False)

m = re.findall('\d\d/[01]\d/\d\d\d\d', '05/22/2023') ; print(True if m else False)
m = re.findall('\d\d/[01]\d/\d\d\d\d', '05/12/2023') ; print(True if m else False)
# =               DD/0M/YYYY
# =               DD/1M/YYYY
m = re.findall('\d\d/[01]\d/\d\d\d\d', '44/12/2023') ; print(True if m else False)

m = re.findall('[0123]\d/[01]\d/\d\d\d\d', '44/12/2023') ; print(True if m else False)
# =                   0D/1M/YYYY
# =                   1D/1M/YYYY
# =                   2D/1M/YYYY
# =                   3D/1M/YYYY

m = re.findall(r'(([012]\d)|([3][01]))/[01]\d/\d\d\d\d', '44/12/2023') ; print(True if m else False)
m = re.findall(r'(([012]\d)|([3][01]))/[01]\d/\d\d\d\d', '30/12/2023') ; print(True if m else False)
m = re.findall(r'(([012]\d)|([3][01]))/[01]\d/\d\d\d\d', '31/12/2023') ; print(True if m else False)
m = re.findall(r'(([012]\d)|([3][01]))/[01]\d/\d\d\d\d', '32/12/2023') ; print(True if m else False)
