"""
5. Write a function that can calculate 
the sum of all even numbers from 1 to 10
with :for loop.
"""
sum = 0
#        range(11) will include 0
for i in range(1, 11):
  if i % 2 ==0:
    sum = sum+i
    # sum += i

print(sum)
