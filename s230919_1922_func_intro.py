import datetime


namsinh    = 1982 
namhientai = datetime.datetime.now().year
tuoi       = namhientai - namsinh
print(f'{namsinh=} {tuoi=}')


print('\n--- thutuc / ham kocotrave \n')


def tinh_tuoi(namsinh):
  namhientai = datetime.datetime.now().year
  tuoi       = namhientai - namsinh
  print(f'{namsinh=} {tuoi=}')

tinh_tuoi(namsinh=1904)
tinh_tuoi(namsinh=1982)
tinh_tuoi(namsinh=2016)


print('\n--- ham co giatritrave return\n')


def tuoi(namsinh):
  namhientai = datetime.datetime.now().year
  tuoi       = namhientai - namsinh
  return tuoi

tuoi1904 = tuoi(namsinh=1904)
tuoi2016 = tuoi(namsinh=2016)

def loaibaohiem(tuoi):
  if             60 <= tuoi : print(f'{tuoi=:<3} baohiem @ nguoi lon tuoi')
  if tuoi < 18              : print(f'{tuoi=:<3} baohiem @ tre em')

loaibaohiem(tuoi=tuoi1904)
loaibaohiem(tuoi=tuoi2016)
