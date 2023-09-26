import random

# n = random.random()
sobimat = random.randint(1,10) # random số từ 1 đến (10-1)
print(sobimat)

n = 0
while True:
  user_guess = input('Mời bạn đoán \n> ') # \n : xuống dòng

  #kiem tra so hop le
  try:
    user_guess = int(user_guess)
  except:
    print(f'Bạn đã nhập {user_guess} - đây không phải số thập phân')
    continue
  
  if user_guess == sobimat:
    print('Chúc mừng bạn đã đoán đúng')
    break
  else:
    if user_guess > sobimat:
      print('Số bạn đoán lớn hơn số bí mật')
    else:
      print('Số bạn đoán nhỏ hơn số bí mật')
  
  n = n + 1
  if n >= 5:    
    print('Bạn đã đoán sai 5 lần rồi')
    break

print('Goodbye')
