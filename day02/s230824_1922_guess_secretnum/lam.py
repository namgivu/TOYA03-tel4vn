import random


# n = random.random()
secret_number = random.randint(1, 10)  # đây là số random từ 1 -> 10
print(secret_number)

count = 0
while True:
    user_guess = input('Mời bạn đoán số:\n> ')
    try: user_guess = int(user_guess)
    except:
      print('Bạn nhập không phải là số thập phân, vui lòng nhập lại!')
      continue

    if int(user_guess) == secret_number:
        print('Bạn quá pro-vip ! \U0001f600 ')
        break
    else:
       if user_guess > secret_number:
         print('Số của bạn hơi lớn \U0001F923')
         s = 4 - count  # nen ghi la s = 5 - count - 1  # 1 la luot hientai
         print(f"Bạn còn {s} lượt")
       else:
         print('Số của bạn nhỏ hơn \U0001F923')
         s = 4 - count
         print(f"Bạn còn {s} lượt")

    count += 1
    if count == 5:
        print('''
        ***=> \U0001F923 BẠN ĐÃ HẾT LƯỢT \U0001F923 <=***
        ''')
        break

print('''
***** ***** ***** ***** ***** ***** *****  *****
*****           \U0001F923  END GAME  \U0001F923           *****
***** ***** ***** ***** ***** ***** *****  *****
''')
