def my_function(n):
  # return sum([i for i in range(1, n+1)  if i % 2 == 0 ])
  return   sum([i for i in range(2, n+1, 2) ])

ans = my_function(n=8)
print(ans)
