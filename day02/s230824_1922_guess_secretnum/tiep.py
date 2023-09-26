import random

secret_number = random.randint(1, 10)
print(secret_number)

n = 0
while True:
  user_number = input('Mời bạn đoán chữ số \n> ')

  try:
    user_number = int(user_number)
  except:
    print(f'Bạn vừa nhập: {user_number} - đây không phải là số nguyên')
    continue

  if user_number == secret_number:
    print(f'✅ Chúc mừng bạn! {secret_number} là chữ số chính xác!')
    break
  else:
    if user_number > secret_number:
      print('Số bạn đoán nên nhỏ hơn tí nè!')
    else:
      print('Nhập số lớn hơn tí tị tì ti nữa nhớ!')

  n = n + 1
  if n >= 5:
    print('Bạn đã đoán số sai 5 lần liên tiếp!')
    break

print('Kết thúc chương trình.')
