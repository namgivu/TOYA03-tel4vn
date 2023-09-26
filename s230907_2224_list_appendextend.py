a = ['dog', 'cat', 'elephant']
print(a)

a.append('mouse')
# a.append('mouse', 'mouse2')  # error
print(a)

a = a + ['mouseagain']
a = a + ['mouseagain', 'mouse2nd']
print(a)

a.extend( ['mouse3', 'mouse3again'] )  # error
#         [                       ] <-- pls mind the list bracket []
print(a)
