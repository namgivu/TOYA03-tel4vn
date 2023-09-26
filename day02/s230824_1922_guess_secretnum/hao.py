import random

# n = random.random()
secret_number = int(random.randint(1, 10))  # random số từ 1 đến (10-1)
print(type(secret_number))
print(secret_number)

count = 0
while True:
  user_guess = input('\nMời bạn đoán số \n> ')

  try:
    user_guess = int(user_guess)  # \n : xuống dòng
  except:
    print('Bạn phải nhập số nguyên, ví dụ : 1,2,3,4')
    continue  # go to next loop-step  vi. chạy tiếp bước kế sau của vòng lặp

  if user_guess < secret_number:
    print('Sô bạn đoán thấp số bí mật 📢 ')
  elif user_guess > secret_number:
    print('Sô bạn đoán cao hơn số bí mật 📢')
  elif user_guess == secret_number:
    print('Bạn đã đooán đúng, bạn thắng ✅')
    break

  count = count + 1  # count += 1
  if count == 5:
    print('Bạn đã hết 5 lần đoán rồi, bạn thua ')
    break

print('Tạm biệt')
