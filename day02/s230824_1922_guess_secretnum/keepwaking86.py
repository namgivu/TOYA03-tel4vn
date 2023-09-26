import random

number = random.randint(1, 10)
i = 0
while (i < 5):
  print("Enter your number")
  my_number = int(input())
  if my_number < number:
    print("Your number is lower", number)
    i = i + 1
    if i == 5:
      print("Game win")
  elif my_number > number:
    print("Your number is higher", number)
    i = i + 1
    if i == 5:
      print("Game win")
  else:
    print("You guess right number", number)
    print("You win")
    break
"""
import random
secret_number=random.randint(1,10)
i=0
while (i<5):
    print("I guess: ")
    my_number=int(input())
    if my_number < secret_number:
        print("My number is lower secret number")
    elif my_number > secret_number:
        print("My number is higher secret number")
    else:
        print("Secret number is",secret_number)
        print("I guess right. I win!!!!")
        break
    i = i + 1
    if i == 5:
        print("Game is win")
"""
