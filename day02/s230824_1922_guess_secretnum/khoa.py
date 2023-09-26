import random

numRand = random.randint(1, 10)

i = 0
while True:
  if i == 5:
    print(f'\n{numRand} mới đúng. QUÁ DỞ!')
    break
  
  try:
    numUser = int(input("Đoán đê\n> "))
  except:
    print('Đây không phải số thập phân.\n')
    continue

  if numUser < numRand:
    print('Lên xíu\n')
  elif numUser > numRand:
    print('Xuống xíu\n')
  else:
    print('Hên thôi\n')
    break

  i = i + 1

print('\nKết Thúc')
