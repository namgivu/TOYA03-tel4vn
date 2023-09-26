"""
5. Write a function that can calculate 
the sum of all even numbers from 1 to 10
with :for loop.
"""
sum = 0
for i in range(2, 10+1, 2):
  sum += i
print(sum)

###

mang = [ i  for i in range(2, 10+1, 2) ]
print(sum(mang))

###

print(
  sum([ i  for i in range(2, 10+1, 2) ])
)
