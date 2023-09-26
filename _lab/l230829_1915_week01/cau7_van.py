def my_function(n):
  sum = 0
  for i in range(1, n+1):
    if i % 2 == 0:
      sum = sum +i
  return sum

ans = my_function(n=8)
print(ans)
