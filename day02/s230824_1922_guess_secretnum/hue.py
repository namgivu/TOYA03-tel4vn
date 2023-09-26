import random

# n = random.random()
secret_number = random.randint(1, 10)  # random so tu 1 den (10-1)
print(secret_number)

count = 0
while True:
    user_guess = input('Mời bạn đoán số \n> ')
  
    try:
    user_guess = int(user_guess)
    except: 
      print(f'Bạn đã nhập {user_guess} không phải là số thập phân')
     continue
  
    if user_guess == secret_number:
        print('✅ Bingo. Chúc mừng bạn đã đoán đúng, quà của bạn đây!')
        break
    else:
        if user_guess > secret_number:
            print('Chưa đúng rồi, số bạn chọn đang lớn hơn số bí mật!')
        else:
            print('Chưa đúng rồi, số bạn chọn đang nhỏ hơn số bí mật!')
    count = count + 1
    if count == 5:
        print('Bạn đã hết lượt!')
        break
print('Hẹn gặp lại')
