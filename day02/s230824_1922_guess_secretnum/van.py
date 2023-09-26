import random

secret_number = random.randint(1, 10)
print(secret_number)

n = 0
while True:
  num = input('Mời pé Hêu đoán số \n>> ')

  try:
    num = int(num)
  except:
    print(f'Pe hêu nhập {num} - không phải là số nguyên')
    continue  # go to next loop-step  vi. chạy tiếp bước kế sau của vòng lặp

  if num == secret_number:
    print('Chim Ưng ✅')
    break
  else:
    if num > secret_number:
      print('Lô hơi lớn!')
    else:
      print('Lô hơi pé!')

  n = n + 1
  if n >= 5:
    print('Pé Hêu tạch lô rồi')
    break

print('Chim Cút')
