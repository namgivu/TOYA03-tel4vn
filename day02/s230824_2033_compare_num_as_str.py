s='1'
t='2'
print(s<t)


# '11' < '2' la True
s='11'
t='2'
print(s<t)

if s<t: print(f's nhohon t  s={s} t={t}')
else  : print( 's KHONG nhohon t')


# 11 < 2 la False
s=11
t=2
print(s<t)

if s<t: print(f's nhohon t        s={s} t={t}')
else  : print(f's KHONG nhohon t  s={s} t={t}')

'''
string compare will go digit by digit fr the left 
it stops at the first digit differs

sosanh chuoi se di tung chucai trong chuoi tubentrai
no se dung lai o chuso dautien khacnhau

122333
1224
   ^ stop at 4 -> '4'>'3' -> '1224' > '122333'
'''
