import random

# n = random.random()
# print(n)
secret_number = random.randint(1, 10)

count = 0
while True:
  user_guess = input("Please choose a number \n> ")
  try: user_guess = int(user_guess)
  except: 
    print ("please input number")
    continue
  if secret_number == user_guess:
    print("ping pong, it is correct")
    break
  elif secret_number > user_guess:
    print("it is wrong, secret is bigger")
  else:
    print("it is wrong, secret is smaller")
  count = count + 1
  if count >= 5:
    print("over 5 times")
    break
print("bye bye :D")
