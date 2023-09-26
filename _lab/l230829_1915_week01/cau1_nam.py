"""
What is the difference between these code in Python? 
Which is variable, which is a string? 
If it is variable, is it valid?

a. 1_string
b. _hello
c. ‘hello’
d. “hello”
e. Hello_1

---

In python, a string must start and end with either 
  quote               "
  single quote        ' 
  trible quote        """
  trible single-quote """

So
choice         is var?    is string?    valid var?
a. 1_string    True       .             False
b. _hello      True       .             True
c. 'hello'     .          True
d. "hello"     .          True
e. Hello_1     True       .             True

0. hello-1     True       .             False
hello-1=122
print(hello-1)
will get error 
>   File "main.py", line 31
    hello-1=122
    ^^^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

1. -hello      True       .             False
"""
