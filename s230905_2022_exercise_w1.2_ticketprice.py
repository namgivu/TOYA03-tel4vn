"""
Write code that will do the following work:
○ Input ”n” as number of people.

○ Input ages of n people.

○ Ticket price is:
■ 25$  / 1 children, which is younger than 18.
■ 100$ / 1 adult,    18 to 60 years old.
■ 50$  / 1 person,   which is older than 60.

○ Calculate the total money of those people’s tickets.
"""

# Input ”n” as number of people.
n = input('Nhập số người\n> ')
n = int(n)

tongtien = 0
for i in range(n):
  age = input(f'Nhap tuoi cho nguoi thu {i+1}\n> ')
  age = int(age)

  '''    - 18 --------- 60 -  '''
  if age < 18:                    price = 25
  elif     18 <= age <= 60:       price = 100
  elif                  60 < age: price = 50

  if age < 18:                    daitu = 'children'
  elif     18 <= age <= 60:       daitu = 'adult'
  elif                  60 < age: daitu = 'person'

  print( 'Giá vé: ',price,'$/1 ',daitu)
  print(f'Giá vé là {price}$ / 1 {daitu}  ')

  tongtien += price
  print()

print(f'''
---
Tongtien {tongtien}$
''')
