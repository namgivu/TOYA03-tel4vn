import random

secret_number = random.randint(1,10)
print(secret_number)

n = 0
while True:
  user_number = input('Mời bạn đoán số \n> ')
  
  # kiemtra so hople
  try:    
    user_number = int(user_number)
  except: 
    print(f'Ban da nhap {user_number} - day khong phai la sothapphan')
    continue  # go to next loop-step  vi. chạy tiếp bước kế sau của vòng lặp

  #
  if user_number == secret_number:
    print('Chúc mừng bạn đã đoán trúng ✅')
    break
  else:
    if user_number > secret_number :
      print('Số bạn đoán lớn hơn tí nè!')
    else:
      print('Số bạn đoán nhỏ hơn tí nè!')
        
  n = n + 1
  if n >= 5:
    
    print('Bạn đã đoán sai 5 lần rồi')
    break
      
print('Bye Bye')
