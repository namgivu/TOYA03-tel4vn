import random

# n = random.random()
secret_number = random.randint(1,10) # so ngau nhien tu 1 den 10-1
print(secret_number)

count = 0
while True:
  user_guess = input('Mời bạn đoán số \n> ') # \n : xuống dòng

  # kiem tra tinh hop le
  try:
    user_guess = int(user_guess)
  except:
    print(f'Bạn đã nhập {user_guess} - không phải là số thập phân')
    continue # chay buoc tiep theo cua vong lap
  
  if user_guess == secret_number:
    print('Chúc mừng. Bạn đã đoán chính xác \N{grinning face}')
    break
  else:
    if user_guess > secret_number:
      print('Số của bạn lớn hơn rồi!')
    else:
      print('Số của bạn nhỏ hơn rồi!')

    count = count + 1 # count +=1
    if count == 5:
      print('Bạn đã đoán 5 lượt chưa chính xác rồi.')
      break
  
print('Tạm biệt')
